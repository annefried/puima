"""

Puima-related utils

Authors: Annemarie Friedrich, Timo Schrader

TODO: make collection ID configurable

July 2021
"""

__author__ = "Annemarie Friedrich and Timo Schrader"
__license__ = "Apache 2.0"
__version__ = "1.0"


import os.path
from puima.pycas import Annotation, PyCas
from puima.default_type_system import defaultTypeSystem

# add other ligatures
ligatures_and_replacement = [('\uFB01', "fi"), ('\uFB02', "fl"), ('\uFB00', 'ff')] # <-- UIMA CAS Viewer does not like '&' and using Unicode shifts the offsets which the viewer also cannot handle
# Chars which need to be replaced in XML
xml_escape_chars = [("&", "&amp;"), ('"', "&quot;"), ("<", "&lt;"), (">", "&gt;") ] # no need to replace appos?

# There are also <span> tags but they are more difficult to remove..
html_tags = ["<i>", "</i>", "<sup>", "</sup>", "<sub>", "</sub>"]
default_xmi_header = """<?xml version="1.0" encoding="UTF-8"?><xmi:XMI xmlns:pos="http:///de/tudarmstadt/ukp/dkpro/core/api/lexmorph/type/pos.ecore" xmlns:tcas="http:///uima/tcas.ecore" xmlns:xmi="http://www.omg.org/XMI" xmlns:cas="http:///uima/cas.ecore" xmlns:tweet="http:///de/tudarmstadt/ukp/dkpro/core/api/lexmorph/type/pos/tweet.ecore" xmlns:morph="http:///de/tudarmstadt/ukp/dkpro/core/api/lexmorph/type/morph.ecore" xmlns:dependency="http:///de/tudarmstadt/ukp/dkpro/core/api/syntax/type/dependency.ecore" xmlns:type5="http:///de/tudarmstadt/ukp/dkpro/core/api/semantics/type.ecore" xmlns:type7="http:///de/tudarmstadt/ukp/dkpro/core/api/transform/type.ecore" xmlns:type6="http:///de/tudarmstadt/ukp/dkpro/core/api/syntax/type.ecore" xmlns:type2="http:///de/tudarmstadt/ukp/dkpro/core/api/metadata/type.ecore" xmlns:type3="http:///de/tudarmstadt/ukp/dkpro/core/api/ner/type.ecore" xmlns:type4="http:///de/tudarmstadt/ukp/dkpro/core/api/segmentation/type.ecore" xmlns:type="http:///de/tudarmstadt/ukp/dkpro/core/api/coref/type.ecore" xmlns:constituent="http:///de/tudarmstadt/ukp/dkpro/core/api/syntax/type/constituent.ecore" xmlns:type9="http:///de/tudarmstadt/ukp/inception/recommendation/api/type.ecore" xmlns:chunk="http:///de/tudarmstadt/ukp/dkpro/core/api/syntax/type/chunk.ecore" xmlns:custom="http:///webanno/custom.ecore" xmlns:type8="http:///de/tudarmstadt/ukp/inception/api/kb/type.ecore" xmi:version="2.0">\n"""
xmi_metainfo = """<type2:DocumentMetaData xmi:id="2" sofa="1" begin="0" end="{3}" language="x-unspecified" documentTitle="{0}" documentId="{1}" documentUri="{2}" collectionId="CollectionID" documentBaseUri="" isLastSegment="false"/>\n"""
xmi_heading = """<type4:Heading xmi:id="{0}" sofa="1" begin="{1}" end="{2}" divType="{3}"/>\n"""
xmi_paragraph = """<type4:Paragraph xmi:id="{0}" sofa="1" begin="{1}" end="{2}" divType="p"/>\n"""
xmi_sentence = """<type4:Sentence xmi:id="{0}" sofa="1" begin="{1}" end="{2}"/>\n"""
xmi_token = """<type4:Token xmi:id="{0}" sofa="1" begin="{1}" end="{2}"/>\n"""
xmi_sofa = """<cas:Sofa xmi:id="1" sofaNum="1" sofaID="_InitialView" mimeType="text" sofaString="{0}"/>\n"""
xmi_casView = """<cas:View sofa="1" members="{0}"/>\n"""


def replace_ligatures(text: str) -> str:
    """
    :param text: input text to be modified
    :return: modified text (ligature replaced)
    """
    for ligature, replacement in ligatures_and_replacement:
        text = text.replace(ligature, replacement)
    return text


def xml_escape(text: str) -> str:
    """
    :param text: input text to be modified
    :return: modified text (ligature replaced)
    """
    for char, replacement in xml_escape_chars:
        text = text.replace(char, replacement)
    return text


def fix_text(text: str) -> str:
    """
    :param text: input text to be modified
    :return: modified text (replaced ligatures + escaped XML chars)
    """
    text = xml_escape(text)
    text = replace_ligatures(text)
    return text


def create_xmi_from_raw_text(text: str, documentId: str, pmcId: str, documentTitle: str, documentUri: str,
                             output_path: str, xmi_header = default_xmi_header) -> None:
    """
    Retrieves raw text and creates a UIMA CAS XMI file body.

    Args:
        text (str): Text to be converted
        documentId (str): Document ID from metadata
        pmcId (str): PMC ID from metadata # TODO: make this optional!
        documentTitle (str): Article Title
        documentUri (str): URI
        output_path (str): output folder (filename will be document ID by default)
    """
    output_string = """"""
    sofa = fix_text(text)
    output_string_headings = ""
    output_string_paragraphs = ""
    output_string_sentences = ""
    output_string_tokens = ""
    xmi_cas_view_members = ""

    output_string += xmi_header
    output_string += xmi_metainfo.format(documentTitle, documentId, documentUri, len(sofa))
    output_string += output_string_headings
    output_string += output_string_paragraphs
    output_string += output_string_sentences
    output_string += output_string_tokens
    output_string += xmi_sofa.format(sofa)
    output_string += xmi_casView.format(xmi_cas_view_members)
    output_string += """</xmi:XMI>"""
    with open(os.path.join(output_path, documentId + ".xmi"), encoding="utf-8", mode="w") as f:
        f.write(output_string)
    return

def create_xmis_from_raw_text_folder(input_path: str, output_path: str, write_type_system=True, write_dkpro_types=False) -> None:
    """
    Reads text files from directory and converts the text content to XMI files.

    Args:
        input_path (str): Path to txt files
        output_path (str): Desired output path
        write_type_system (bool, optional): Whether to write UIMA CAS TypeSystem.xml to output path. Defaults to True.
        write_dkpro_types (bool, optional): Whether to include Inception XMI tags. Defaults to False.
    """
    # Read in a document collection.
    text_collection = [f for f in os.listdir(input_path) if f.endswith(".txt")]
    if write_type_system:
        with open(os.path.join(output_path, "TypeSystem.xml"), encoding="utf-8", mode="w") as ts:
            ts.write(defaultTypeSystem)
    if not write_dkpro_types:
        global xmi_header
        global xmi_heading
        global xmi_metainfo
        global xmi_paragraph
        global xmi_sentence
        global xmi_token
        xmi_header = """<?xml version="1.0" encoding="UTF-8"?><xmi:XMI xmlns:pos="http:///de/tudarmstadt/ukp/dkpro/core/api/lexmorph/type/pos.ecore" xmlns:tcas="http:///uima/tcas.ecore" xmlns:xmi="http://www.omg.org/XMI" xmlns:cas="http:///uima/cas.ecore" xmlns:tweet="http:///de/tudarmstadt/ukp/dkpro/core/api/lexmorph/type/pos/tweet.ecore" xmlns:morph="http:///de/tudarmstadt/ukp/dkpro/core/api/lexmorph/type/morph.ecore" xmlns:dependency="http:///de/tudarmstadt/ukp/dkpro/core/api/syntax/type/dependency.ecore" xmi:version="2.0">"""
        #xmi_metainfo = xmi_metainfo.replace("type2:", "")
        xmi_heading = xmi_heading.replace("type4:", "")
        xmi_paragraph = xmi_paragraph.replace("type4:", "")
        xmi_sentence = xmi_sentence.replace("type4:", "")
        xmi_token = xmi_token.replace("type4:", "")
    for text_file in text_collection:
        with open(os.path.join(input_path, text_file), encoding="utf-8", mode="r") as file:
            text = file.read()

        # SET METADATA
        docID = text_file
        pmcID = None
        uri = text_file
        title = text_file

        create_xmi_from_raw_text(text, docID, pmcID, title, uri, output_path)
    return


def rename_annotations(cas: PyCas, original_type_name: str, new_type_name: str, features: list):
    """
    Renames annotation of a particular types to a different one.
    :param cas: PyCas
    :param original_type_name: original type name
    :param new_type_name: new type name
    :param features: list of features, given as tuples with name and a boolean indicating whether it is a reference to
        another annotation.
    """
    annots_to_remove = set()

    for annot in cas.select_annotations(original_type_name):
        annots_to_remove.add(annot)

    for annot in annots_to_remove:
        new_annot = Annotation(cas, None, new_type_name, annot.begin, annot.end)
        for feat, is_reference in features:
            try:
                new_annot.set_feature_value(feat, annot.get_feature_value(feat, is_reference), is_reference)
            except:
                pass
        new_annot.add_to_indices()
        annot.remove_from_indices()


def same_span(annot1, annot2):
    """
    Returns true if annot1 and annot2 cover the exact same span.
    :param annot1: Annotation
    :param annot2: Annotation
    :return: bool
    """
    return annot1.begin == annot2.begin and annot1.end == annot2.end


def overlap(annot1, annot2):
    """
    Returns true if annot1 and annot2 overlap (but do not cover the exact same span).
    :param annot1: Annotation
    :param annot2: Annotation
    :return: bool
    """
    if annot1.begin <= annot2.begin < annot1.end:
        return True
    if annot2.begin <= annot1.begin < annot2.end:
        return True
    return False


def remove_annotations_from_indices(annot_list):
    """
    Clears a list of annotations from its PyCas.
    :param annot_list: list of Annotation objects
    """
    for annot in annot_list:
        annot.remove_from_indices


def add_annotations_to_indices(annot_list):
    """
    Adds a list of annotations to a PyCas.
    :param annot_list: list of Annotation objects
    """
    for annot in annot_list:
        annot.add_to_indices()
