"""
Puima: a lightweight Python-framework to process the text part of UIMA CAS structures.

This file contains modules for accessing CAS structures in Python.
"""

__author__ = "Annemarie Friedrich, and Timo Schrader"
__license__ = "Apache 2.0"
__version__ = "1.0"

# coding=utf-8

from lxml import etree
import io
from bisect import bisect_left, bisect_right

xmlParser = etree.XMLParser(remove_blank_text=True)

XMI_ATTRIBUTES = {"xmi:id", "begin", "end", "Governor", "Dependent", "sofa"}
# ignoring sofa because we assume that for text analysis, there will always be exactly one SOFA

global typePrefixMap
global typePrefixMapInv

typePrefixMap = {}
typePrefixMapInv = {}

class Index:
    """
    Annotation indices.
    """

    def __init__(self, keyfunction):
        self.seq = []  # list containing annotations in some sorted way
        self.keys = []  # sorted keys of the sorted data (for fast access)
        self.keyfunc = keyfunction


    # see https://stackoverflow.com/questions/27672494/how-to-use-bisect-insort-left-with-a-key
    def insert(self, item):
        """Insert an item into a sorted list using a separate corresponding
           sorted keys list and a keyfunc() to extract the key from each item.
        Based on insert() method in SortedCollection recipe:
        http://code.activestate.com/recipes/577197-sortedcollection/
        """
        k = self.keyfunc(item)  # Get key.
        i = bisect_left(self.keys, k)  # Determine where to insert item.
        self.keys.insert(i, k)  # Insert key of item to keys list.
        self.seq.insert(i, item)  # Insert the item itself in the corresponding place.


    def find(self, item):
        k = self.keyfunc(item)  # get key
        return bisect_left(self.keys, k)  # returns index where key value is in between the two elements


    def find_right(self, item):
        k = self.keyfunc(item)
        return bisect_right(self.keys, k)


    def remove(self, item):
        """
        Remove an item from the list
        :param item: The item to be removed.
        :return: Nothing.
        """
        i = self.find(item)
        del self.keys[i]
        del self.seq[i]

class FeatureNotDefinedException(Exception):
    pass


class AnnotationSpan:
    """
    Just a helper class for when dealing with the indices.
    """

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end


class Annotation:
    """
    Objects of this class represent one annotation on text.
    """

    def __init__(self, pycas, id, anno_type, begin, end, dom_object=None):
        """
        :param pycas: the PyCas object.
        :param anno_type: type of annotation (qualified name)
        :param begin: begin char offset of this annotation on the underlying document text
        :param end: end char offset of this annotation on the underlying document text
        :param dom_object: Sets the reference to the relevant part of the DOM in the PyCas object.
        Important for writing out the PyCas as XMI at some point!
        """
        self.pycas = pycas
        self.type = anno_type
        self.begin = begin
        self.end = end

        if id is not None:  # ID already assigned and given in init call (e.g. in XMI)
            if pycas.doc_collection.maxId is None:
                pycas.doc_collection.maxId = id
            else:
                # Important: this can only happen AFTER the entire document collection has already been read in
                pycas.doc_collection.maxId = max(pycas.doc_collection.maxId, id)  # update maxId
        self.id = id

        if dom_object is not None:
            self.dom = dom_object
        else:
            # new annotation, create DOM object and insert into overall dom
            # generate new id
            pycas.doc_collection.maxId += 1
            self.id = pycas.doc_collection.maxId
            typePrefix = ".".join(self.type.split(".")[:-1])
            shortname = self.type.split(".")[-1]
            if typePrefix not in self.pycas.type_to_namespace:
                # for new types (that are only in TypeSystem.xml and not yet in any XMI)
                typePrefixMapInv[typePrefix] = typePrefix
                typePrefixMap[typePrefix] = typePrefix
                prefix = "http:///" + typePrefix.replace(".", "/") + ".ecore"
                self.pycas.type_to_namespace[typePrefix] = prefix
                self.pycas.namespace_to_type[prefix] = typePrefix
            else:
                prefix = self.pycas.type_to_namespace[typePrefix]
            element = etree.Element(etree.QName(prefix, shortname))
            element.attrib[etree.QName("http://www.omg.org/XMI", "id")] = str(self.id)
            element.attrib["begin"] = str(begin)
            element.attrib["end"] = str(end)
            element.attrib["sofa"] = self.pycas.sofa
            self.pycas.root.append(element)
            self.dom = element


    def add_to_indices(self):
        self.pycas.annotations[self.id] = self
        self.pycas.annot_by_type_begin[self.type].insert(self)
        self.pycas.annot_by_type_end[self.type].insert(self)


    def remove_from_indices(self):
        # remove from DOM
        p = self.dom.getparent()
        p.remove(self.dom)
        # remove from indices
        del self.pycas.annotations[self.id]
        self.pycas.annot_by_type_begin[self.type].remove(self)
        self.pycas.annot_by_type_end[self.type].remove(self)
        del self


    def set_begin_and_end(self, begin, end):
        """ remove from indices (without deleting the annotation),
        updating indices in DOM, adding back to index """
        self.pycas.annot_by_type_begin[self.type].remove(self)
        self.pycas.annot_by_type_end[self.type].remove(self)
        self.dom.attrib["begin"] = str(begin)
        self.dom.attrib["end"] =  str(end)
        self.begin = begin
        self.end = end
        self.pycas.annot_by_type_begin[self.type].insert(self)
        self.pycas.annot_by_type_end[self.type].insert(self)


    def get_feature_value(self, name, valueTypeIsAnnotation=False, stringList=False):
        """
        Returns a feature value as a string. Does not yet implement feature structure lists, stringLists are implemented.
        :param name: retrieve feature value for given feature name
        :param valueTypeIsAnnotation: if True, assume that the type of the value is an annotation itself and return the
        corresponding object.
        :param stringList: if True, assume that the type of value is a StringArray (in XML: children of this name of the Annotation node)
        :return: feature value for this name
        """
        # check type of this feature
        t = self.pycas.types[self.type]
        if name not in t.all_features:
            raise FeatureNotDefinedException("Feature " + name + " not defined for type " + self.type)
        feature = t.all_features[name]
        if valueTypeIsAnnotation:
            if feature.rangetype not in self.pycas.types:
                raise Exception("Annotation type requested: " + feature.rangetype + "is not defined in TypeSystem.")
            # treat value of this feature as Annotation id, retrieve the corresponding annotation object
            anno_id = int(self.dom.get(name))
            return self.pycas.annotations[anno_id]
        elif stringList:
            # return a list of the relevant strings
            l = []
            for c in self.dom:
                if c.tag == name:
                    l.append(c.text)
            return l

        if not valueTypeIsAnnotation and not stringList:
            return self.dom.get(name)
            # if feature.rangetype == "uima.cas.String":
            # TODO add check if attribute exists, return None otherwise
            # TODO treat other types of ranges, e.g. Integer / Float
            # TODO conversions to strings for DOM will be expensive on the long run, introduce objects instead?


    def set_feature_value(self, name, value, valueRefersToAnnotation=False, stringList=False):
        """
        Set value for a particular feature. If value is an Annotation object, indicate this by setting valueRefersToAnnotation
        to True.
        :param name: Name of the feature.
        :param valueRefersToAnnotation: whether value refers to some annotation.
        :param stringList: if True, assume that the type of value is a StringArray (in XML: children of this name of the Annotation node)
        :return: nothing
        """
        # check type of this feature
        t = self.pycas.types[self.type]
        if name not in t.all_features:
            raise Exception("Feature " + name + " not defined for type " + self.type)
        if valueRefersToAnnotation:
            self.dom.attrib[name] = str(value.id)
        elif stringList:
            # remove old list if any
            for c in self.dom:
                if c.tag == name:
                    self.dom.remove(c)
            # create new list
            for v in value:
                e = etree.SubElement(self.dom, name)
                e.text = v
        else:
            self.dom.attrib[name] = str(value)
    # TODO general FSLists are not implemented yet

    def __str__(self):
        return self.type + " begin:" + str(self.begin) + " end:" + str(self.end)


class PyCas:
    """
    Objects of this class represent the Common Analysis Structure (CAS) for one Subject Of Analysis (SOFA),
    usually one text document.
    IMPORTANT! Access the data of this object EXCLUSIVELY via the getter / setter methods. If you feel something
    is missing, please contact the developers!

    Constructing PyCas from raw text files is not currently supported: would have to run through some UIMA engine
    first and generate XMI.
    """
    def __init__(self, doc_collection, xmi_input_file):

        with io.open(xmi_input_file, 'r', encoding="utf-8") as f:
            self.dom = etree.parse(f, xmlParser)
        self.root = self.dom.getroot()
        self.namespace_to_type = {}
        self.type_to_namespace = {}

        self.doc_collection = doc_collection
        self.types = doc_collection.typeSystem.types  # reference to type system
        self.annotations = {}  # map: annotation ID to annotation object

        # indices
        self.annot_by_type_begin = {}
        self.annot_by_type_end = {}
        for t in self.types:
            self.annot_by_type_begin[t] = Index(lambda a: a.begin)  # sorted by begin index
            self.annot_by_type_end[t] = Index(lambda a: a.end)  # sorted by end index

        # XML namespace defines the long type names (including package names)
        for shortname in self.root.nsmap:
            long = self.root.nsmap[shortname][8:-6].replace("/", ".")
            self.namespace_to_type[self.root.nsmap[shortname]] = long
            self.type_to_namespace[long] = self.root.nsmap[shortname]
            typePrefixMap[shortname] = long
            typePrefixMapInv[long] = shortname

        for element in self.root:
            # CAS-SOFA-related stuff
            if element.tag.endswith("NULL") or element.tag.endswith("View") or element.tag.endswith("TagDescription"):
                # ignoring these entries
                # TODO do we need TagDescription in namespace?
                continue
            elif element.tag.endswith("Sofa"):
                self.doc_text = element.get("sofaString")
            else:
                # Regular annotations
                long, short = element.tag.split("}")
                if long[1:] not in self.namespace_to_type:
                    # for new annotations, namespace not in upper element, but just in individual elements
                    # TODO fix that elsewhere, would be nicer than the workaround here!
                    typename = long[1:][8:-6].replace("/", ".")
                    self.namespace_to_type[long[1:]] = typename
                    self.type_to_namespace[typename] = long
                    typePrefixMap[short] = typename
                    typePrefixMapInv[typename] = short
                long = self.namespace_to_type[long[1:]]
                typeName = long + "." + short
                if typeName == "de.tudarmstadt.ukp.dkpro.core.api.metadata.type.DocumentMetaData":
                    self.doc_meta_data = element
                    self.sofa = element.attrib["sofa"]
                # create Annotation object
                try:
                    id = int(element.get("{http://www.omg.org/XMI}id"))
                except:
                    print(typeName)
                # temporary fix for the new annotations that don't have offsets
                begin = element.get("begin")
                end = element.get("end")
                if begin is not None:
                    begin = int(begin)
                else:
                    begin = 0
                if end is not None:
                    end = int(end)
                else:
                    end = 0
                annot = Annotation(self, id, typeName, begin, end, element)
                annot.add_to_indices()


    def check_meta_data_exists(self, attribute=None):
        if self.doc_meta_data is None:
            raise Exception
        if attribute is not None:
            if attribute not in self.doc_meta_data.keys():
                raise Exception


    def get_doc_uri(self):
        self.check_meta_data_exists("documentUri")
        return self.doc_meta_data.get("documentUri")


    def set_doc_uri(self, value):
        self.check_meta_data_exists()
        self.doc_meta_data.attrib["documentId"] = value


    def get_doc_id(self):
        """
        Assumes there is exactly one DocumentMetaData annotation per PyCas.
        :return: the unique document ID (for now set externally by UIMA code)
        """
        self.check_meta_data_exists("documentId")
        return self.doc_meta_data.get("documentId")


    def set_doc_id(self, value):
        """
        This method allows for changing the document ID.
        :param doc_id: new document ID.
        :return: Nothing.
        """
        self.check_meta_data_exists()
        self.doc_meta_data.attrib["documentId"] = value


    def get_language(self):
        """
        :return: the document language as given in DocumentMetaData.
        """
        self.check_meta_data_exists("language")
        return self.doc_meta_data.get("language")


    def set_language(self, value):
        """
        Setter for the document language.
        :param value: string specifying the language (please refer to dkpro documentation).
        :return: Nothing.
        """
        self.check_meta_data_exists()
        self.doc_meta_data.attrib["language"] = value


    def get_doc_text(self):
        """
        :return: Document text (SOFA string).
        """
        return self.doc_text


    def get_covered_text_span(self, begin, end):
        return self.doc_text[begin:end]


    def get_covered_text(self, annotation):
        return self.doc_text[annotation.begin:annotation.end]


    def select_annotations(self, typename):
        """
        :param t: type object.
        :return: Iterates over all annotations of type t. Equivalent of JCasUtil.select(...)
        """
        for typename in [typename] + [st.name for st in self.types[typename].subtypes]:
            for annotation in self.annot_by_type_begin[typename].seq:
                yield annotation


    def select_covered(self, typename, annotation):
        """
        :param typename: string name of the type of the annotations that are to be returned.
        :param annotation: the covering annotation.
        :return: all annotations of a particular type that are covered by a particular annotation.
        """
        # repeat for type and all its subtypes
        for typename in [typename] + [st.name for st in self.types[typename].subtypes]:
            # check if there are annotations of this type at all
            if len(self.annot_by_type_begin[typename].seq) == 0:
                continue
            # get start in list (comparing begin) quickly
            i = self.annot_by_type_begin[typename].find(annotation)
            # if end of sequence is returned, nothing found TODO double-check
            if i == len(self.annot_by_type_begin[typename].seq):
                continue
            while i < len(self.annot_by_type_begin[typename].seq):
                anno = self.annot_by_type_begin[typename].seq[i]
                i += 1
                if anno is annotation:
                    # don't return the annotation itself
                    continue
                if anno.begin > annotation.end or anno.end < annotation.begin:  # last part of condition just for safety
                    break
                if anno.begin >= annotation.begin and anno.end <= annotation.end:
                    yield anno


    def select_covered_span(self, typename, begin, end):
        """
        :param typename: The type of the annotations to be returned.
        :param begin: begin index of the span in which to search.
        :param end: end index of the span in which to search.
        :return: all annotations of a particular type that are covered by the given span.
        """
        return self.select_covered(typename, AnnotationSpan(begin, end))


    def select_covering(self, typename, annotation):
        """
        Use with care, not as quick as select_covered in most cases!! Always access / combine annotations using
        select_covered if possible!

        :param typename: string name of the type of the annotations that are to be returned.
        :param annotation: the annotation covered by the annotations to be returned.
        :return: all annotations of a particular type that are covering a particular annotation.
        """
        for typename in [typename] + [st.name for st in self.types[typename].subtypes]:
            # select set of annotations where begin is smaller or equal to given annotation
            i = self.annot_by_type_begin[typename].find_right(annotation)
            candidates = set(self.annot_by_type_begin[typename].seq[:i])
            # select set of annotations where end is equal to or greater than given annotation
            j = self.annot_by_type_end[typename].find(annotation)
            candidates2 = set(self.annot_by_type_end[typename].seq[j:])
            # form intersection, yield those
            for anno in candidates & candidates2:
                if anno.begin <= annotation.begin and anno.end >= annotation.end:
                    # something is wrong above, ideally this check should not be required
                    yield anno


    def select_covering_span(self, typename, begin, end):
        return self.select_covering(typename, AnnotationSpan(begin, end))


    def serialize(self, xmi_output_path):
        """
        Serializes this PyCas back to XMI output format.
        :param xmi_output_path: where to write the XMI file.
        :return:
        """
        # update view members in DOM
        members = " ".join(str(id) for id in self.annotations.keys())
        viewEl = self.root.find("{http:///uima/cas.ecore}View")
        viewEl.attrib["members"] = members
        viewSofa = self.root.find("{http:///uima/cas.ecore}Sofa")
        # these two have to be at the end of the XMI document (otherwise UIMA ignore any annotations after them)
        self.root.remove(viewEl)
        self.root.remove(viewSofa)
        self.root.append(viewSofa)
        self.root.append(viewEl)
        # write XML
        if not xmi_output_path.endswith(".xmi"):
            xmi_output_path = xmi_output_path + ".xmi"
        self.dom.write(xmi_output_path, pretty_print=True, xml_declaration=True, encoding="utf-8")