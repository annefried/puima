"""
Puima: a lightweight Python-framework to process the text part of UIMA CAS structures.

Deals with the relevant part of the UIMA type system.
Assumes that the type system for all documents in the collection is the same and given in TypeSystem.xml.
If you are making any changes to the type system (only additions of types or features are allowed!!!),
please update TypeSystem.xml accordingly and deliver this updated file with your processed document collection.
"""

__author__ = "Annemarie Friedrich"
__license__ = "Apache 2.0"
__version__ = "1.0"

import xml.dom.minidom as minidom
import io


class Feature:

    def __init__(self, name, description, rangetype):
        self.name = name
        self.description = description
        self.rangetype = rangetype  # type of this feature

    def __str__(self):
        return "Feature: " + self.name + " range: " + self.rangetype


class Type:
    """
    Represents one type definition.
    """
    def __init__(self, name, description, supertype):
        self.name = name
        self.shortname = name.split(".")[-1]
        self.supertype = supertype
        self.description = description
        self.subtypes = set()
        self.features = set()
        self.all_features = {}  # includes features defined in supertypes

    def add_feature(self, feature):
        """
        Use this method to register a new feature for this type.
        :param feature: feature object representing a feature
        :return: doesn't return anything
        """
        self.features.add(feature)


class TypeSystem:

    def __init__(self, typesystem_xml):
        self.types = {}  # map from type names to the type objects
        with io.open(typesystem_xml, 'r', encoding="utf-8") as f:
            dom = minidom.parse(f)
        # UIMA built in type(s)
        annotype = Type("uima.tcas.Annotation", "built-in supertype for annotations", None)
        self.types[annotype.name] = annotype
        # read types from application type system
        for typeDesc in dom.getElementsByTagName("typeDescription"):
            name = typeDesc.getElementsByTagName("name")[0].firstChild.data.strip()
            if len(typeDesc.getElementsByTagName("description")[0].childNodes) > 0:
                description = typeDesc.getElementsByTagName("description")[0].firstChild.data
            else:
                description = None
            supertype = typeDesc.getElementsByTagName("supertypeName")[0].firstChild.data
            t = Type(name, description, supertype)
            # add features
            for feature in typeDesc.getElementsByTagName("featureDescription"):
                name = feature.getElementsByTagName("name")[0].firstChild.data
                if len(feature.getElementsByTagName("description")[0].childNodes) > 0:
                    description = feature.getElementsByTagName("description")[0].firstChild.data
                else:
                    description = None
                rangetype = feature.getElementsByTagName("rangeTypeName")[0].firstChild.data
                t.add_feature(Feature(name, description, rangetype))
            self.types[t.name] = t

        # after all types have been read in, generate complete list of features for each type and add subtype
        # information to each type (for retrieval of annotations)
        for t in self.types.values():
            for f in self.get_features(t.name):
                t.all_features[f.name] = f
            # register this type as subtype in all its supertypes
            self.types["uima.tcas.Annotation"].subtypes.add(t)
            while t.supertype in self.types:
                st = self.types[t.supertype]
                st.subtypes.add(t)
                t = st

    def get_features(self, typename):
        """ Generates a list of features available for this type.
        :param typename: the name of the type (string)
        :return: list of features for this type (Feature objects)
        """
        if typename not in self.types:
            raise Exception("Typename " + typename + " is not defined in TypeSystem.")
        t = self.types[typename]
        for ft in t.features:
            yield ft
        if t.supertype in self.types:
            st = self.types[t.supertype]
            if type(st) != str:
                for ft in self.get_features(st.name):
                    yield ft


