"""
Puima: a lightweight Python-framework to process the text part of UIMA CAS structures.

Utilities for reading in / writing out a collection of XMI documents.

Note: Begins and ends are weird for "empty" paragraphs in dkpro.
"""

__author__ = "Annemarie Friedrich and Timo Schrader"
__license__ = "Apache 2.0"
__version__ = "1.0"

import os, shutil
from puima.pycas import PyCas, Annotation
from puima.typesystem import TypeSystem

verbatim = False

class DocumentCollection:
    """
    Represents a document collection.
    """

    def __init__(self, xmi_dir: str, file_list=None) -> None:
        """
        Initializes a new UIMA document collection.

        Args:
            xmi_dir (str): Path to XMI files.
            file_list (list, optional): If provided, only the files in this list will be loaded into the doc collection.
                Files names will be joined with xmi_dir. Defaults to None.
        """
        self.docs = {}
        self.ids = set()  # set of IDs of annotations in the document collection
        self.maxId = None
        # read type system from XML
        self.typeSystem = TypeSystem(os.path.join(xmi_dir, "TypeSystem.xml"))
        self.input_xmi_dir = xmi_dir
        # for now indexes both long and short names of the types

        input_files_names: list = None
        if file_list is not None:
            input_files_names = sorted([f for f in file_list if f in os.listdir(xmi_dir)])
        else:
            input_files_names = sorted(os.listdir(xmi_dir))

        # read XMI files into PyCas
        i = 0
        for filename in input_files_names:
            if not filename.endswith(".xmi"):
                print("ignoring:", filename)
                continue
            if verbatim:
                print("Reading file:", filename)
            pycas = PyCas(self, os.path.join(xmi_dir, filename))
            if pycas.get_doc_id() in self.docs:
                pycas.set_doc_id(pycas.get_doc_id() + str(i))
                i+=1
                # TODO fix input files!
                #raise Exception("Something is wrong with the document IDs - found duplicate for: " + pycas.get_doc_id())
            self.docs[pycas.get_doc_id()] = pycas

    def get_annotation_id(self):
        """
        Generates a new annotation ID. They need to be unique across the entire document collection.
        :return: integer representing ID for new annotation
        """
        
    def get_docs(self):
        """
        convenience method to iterate over the documents.
        :return: yiels one PyCas at a time.
        """
        for doc in self.docs.values():
            yield doc

    def serialize(self, xmi_out_dir):
        """
        Write all files in this document collection to the specified output directory.
        :param xmi_out_dir: path to (existing) directory where output files should be written.
        :return: Nothing
        """
        for d in self.docs.values():
            d.serialize(os.path.join(xmi_out_dir, d.get_doc_id()))
        # copy TypeSystem
        shutil.copyfile(os.path.join(self.input_xmi_dir, "TypeSystem.xml"), os.path.join(xmi_out_dir, "TypeSystem.xml"))