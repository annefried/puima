#!/usr/bin/env python
"""
Puima: a lightweight Python-framework to process the text part of UIMA CAS structures.

Fix a couple of "bugs" in the input files such that PUIMA / INCEpTION don't throw any errors (e.g., invalid characters, document IDs, ...).
Make sure this is run from the project level.
"""

__author__ = "Annemarie Friedrich"
__license__ = "Apache 2.0"
__version__ = "1.0"


import os
import sys
import re
from copy import deepcopy
import shutil

sys.path.append(os.path.join(os.getcwd(), "..", "puima"))
from puima.collection_utils import DocumentCollection
from puima.pycas import Annotation


# Some regexes
regex1 = re.compile(r'documentTitle="[^"]+"')
regex2 = re.compile(r'documentId="[^"]+"')
regex3 = re.compile(r'documentUri="[^"]+"')
regex4 = re.compile(r'collectionId="[^"]+"')
regex5 = re.compile(r'documentBaseUri="[^"]+"')

def removeInvalidChars(s, minChar:int, maxChar:int):
    new_s = ""
    for c in s:
        if ord(c) >= minChar and ord(c) <= maxChar:
            new_s += c
    return new_s

def fix_filenames(input_dir, output_dir):
    print("Fixing filenames of XMI files in folder:", input_dir)
    for filename in os.listdir(input_dir):
        new_filename = removeInvalidChars(filename, 22, 127) # ASCII range
        shutil.copy(os.path.join(input_dir, filename), os.path.join(output_dir, new_filename))
    if not os.path.exists(os.path.join(output_dir, "TypeSystem.xml")):
        shutil.copy(os.path.join(input_dir, "TypeSystem.xml"), os.path.join(output_dir, "TypeSystem.xml"))



def fix_typenames_etc(input_dir, output_dir):
    """
    :param input_dir: directory where to read XMI files from (as text)
    :param output_dir: directory where to write XMI files
    """
    print("Fixing type names of XMI files in folder:", input_dir)
    for filename in os.listdir(input_dir):
        basename = filename[:-4]
        print(basename)
        with open(os.path.join(input_dir, filename), encoding="utf-8") as f:
            file_content = f.read()
        # replace documentTitle and documentId
        file_content = re.sub(r'documentTitle="[^"]+"', 'documentTitle="' + basename + '"', file_content)
        # print(regex1.search(file_content))
        file_content = re.sub(regex2, 'documentId="' + basename + '"', file_content)
        # print(regex2.search(file_content))
        file_content = re.sub(regex3, 'documentUri="' + basename + '"', file_content)
        file_content = re.sub(regex4, 'collectionId="ml_ms_corpus"', file_content)
        file_content = re.sub(regex5, 'documentBaseUri="ml_ms_corpus/' + basename + '"', file_content)

        # invalid chars
        file_content = file_content.replace("&#12", "&#32")
        file_content = file_content.replace("&#10", "&#32")
        for i in range(1, 32):
            file_content = file_content.replace("&#" + str(i) + ";", "&#32;")

        with open(os.path.join(output_dir, filename), 'w', encoding="utf-8") as f:
            f.write(file_content)

        if not os.path.exists(os.path.join(output_dir, "TypeSystem.xml")):
            shutil.copy(os.path.join(input_dir, "TypeSystem.xml"), os.path.join(output_dir, "TypeSystem.xml"))


if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    if os.path.exists(output_path + "_temp"):
        shutil.rmtree(output_path + "_temp")
    os.makedirs(output_path)
    os.makedirs(output_path + "_temp")
    fix_filenames(input_path, output_path + "_temp")
    fix_typenames_etc(output_path + "_temp", output_path)
    shutil.rmtree(output_path + "_temp")