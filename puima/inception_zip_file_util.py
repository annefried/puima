"""
Puima: a lightweight Python-framework to process the text part of UIMA CAS structures.

Utility script to unzip and re-zip Inception projects in "Webanno"/"INCEpTION" format.
You can run the script on files extracted using the "UIMA XML 1.1" format.

"""

__author__ = "Annemarie Friedrich"
__editor__ = "Hanna Schmueck"
__license__ = "Apache 2.0"
__version__ = "1.0"

from zipfile import ZipFile, is_zipfile
import os, shutil, sys
from puima.fix_xmi import fix_typenames_etc

def unzip_archive(top_path, in_path, out_path, zip_name, annotator_of_interest, annotator_outpath, curation):
    """
    :param top_path: top-level path
    :param in_path: path to zip archive (INCEpTION export)
    :param zip_name: filename of the zip archive
    :param out_path: where to write the unzipped files
    :param annotator_of_interest: only the annotations of this annotator are kept!
    :return:
    """
    in_path = os.path.join(top_path, in_path, zip_name)
    out_path = os.path.join(top_path, out_path)
    xmi_out_path = os.path.join(top_path, annotator_outpath)  # path where to write the relevant XMI files

    if os.path.exists(xmi_out_path):
        shutil.rmtree(xmi_out_path)
    os.makedirs(xmi_out_path)

    print("Unzipping:", in_path)

    # unzip first level
    with ZipFile(in_path, 'r') as zf:
        print('Extracting all the files now...')
        zf.extractall(out_path)
        print('Done!')



    annotations_folder = "annotation"
    if curation == "true":
        annotations_folder = "curation"

    # unzip inner levels
    try:
        for folder in os.listdir(os.path.join(out_path, annotations_folder)):
            print(folder)
            for zipfilename in os.listdir(os.path.join(out_path, annotations_folder, folder)):
                if not is_zipfile(os.path.join(out_path, annotations_folder, folder, zipfilename)):
                    continue
                print("\t", zipfilename)
                zf = ZipFile(os.path.join(out_path, annotations_folder, folder, zipfilename), 'r')
                zf.extractall(os.path.join(out_path, annotations_folder, folder))

                # copy file to xmi_docs folder, changing the filename
                shutil.copy(os.path.join(out_path, annotations_folder, folder, "TypeSystem.xml"),
                                os.path.join(xmi_out_path))
                if os.path.exists(os.path.join(out_path, annotations_folder, folder, annotator_of_interest + ".xmi")):
                    target_loc = folder
                    if not target_loc.endswith(".xmi"):
                        target_loc += ".xmi"
                    shutil.copy(os.path.join(out_path, annotations_folder, folder, annotator_of_interest + ".xmi"),
                                os.path.join(xmi_out_path, target_loc))
    except FileNotFoundError as fnf:
        out_path = os.path.join(out_path, zip_name[:-4])
        for folder in os.listdir(os.path.join(out_path, annotations_folder)):
            print(folder)
            for zipfilename in os.listdir(os.path.join(out_path, annotations_folder, folder)):
                if not is_zipfile(os.path.join(out_path, annotations_folder, folder, zipfilename)):
                    continue
                print("\t", zipfilename)
                zf = ZipFile(os.path.join(out_path, annotations_folder, folder, zipfilename), 'r')
                zf.extractall(os.path.join(out_path, annotations_folder, folder))

                # copy file to xmi_docs folder, changing the filename
                shutil.copy(os.path.join(out_path, annotations_folder, folder, "TypeSystem.xml"),
                                os.path.join(xmi_out_path))
                if os.path.exists(os.path.join(out_path, annotations_folder, folder, annotator_of_interest + ".xmi")):
                    target_loc = folder
                    if not target_loc.endswith(".xmi"):
                        target_loc += ".xmi"
                    shutil.copy(os.path.join(out_path, annotations_folder, folder, annotator_of_interest + ".xmi"),
                                os.path.join(xmi_out_path, target_loc))
    # count number of XMIs found
    count = 0
    for filename in os.listdir(xmi_out_path):
        if filename.endswith("xmi"):
            count += 1
    print("Found", count, "XMI documents from annotator", annotator_of_interest)


if __name__ == '__main__':
    # Usage: 
    base_path = sys.argv[1]  # the base folder where we are operating, INCEpTION export as zip should be in this folder
    source_path = sys.argv[2] # Zip file is the export as UIMA XMI 1.1 from Inception
    target_path = sys.argv[3] # path for extracted zip files
    zip_name = sys.argv[4]
    userid = sys.argv[5]  # the Inception userid of the user whose annotations are to be extracted as XMI documents
    annotator_outpath = sys.argv[6]
    final_target_path = sys.argv[7]  # folder with XMI documents with fixed document name attributes in XMI
    if curation not in ["true", "false"]:
        print("curation needs to be true or false, if false: extrating from annotations folder.")
    unzip_archive(base_path, source_path, target_path, userid, curation)
    if os.path.exists(os.path.join(base_path, final_target_path)):
        shutil.rmtree(os.path.join(base_path, final_target_path))
    
    os.makedirs(os.path.join(base_path, final_target_path))
    fix_typenames_etc(os.path.join(base_path, annotator_outpath), os.path.join(base_path, final_target_path))

    if os.path.exists(os.path.join(base_path, annotator_outpath)):
        shutil.rmtree(os.path.join(base_path, annotator_outpath))

    # Further example usage:
    # This script puts the unzipped file into "extracted_file"
    # unzip_archive(top_path="", in_path="data", zip_name="sample_project.zip", out_path="data/output", annotator_of_interest="annotator.id", curation=False)
