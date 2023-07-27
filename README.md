
# Puima
## A lightweight Python-framework for processing the text part of UIMA CAS structures.

Developed by Annemarie Friedrich and Timo Schrader.

Hint: a more comprehensive library is [DkPro Cassis](https://github.com/dkpro/dkpro-cassis).
Puima is more lightweight, focusing on reading and modification of CASes. While it's fast, we leave verifying the data structures to the client code.

## Usage
The main usage of this code assumes that you already have XMI files that you want to read or modify (e.g., annotated files that you downlaoded from [INCEpTION](https://inception-project.github.io/)).
Hence, the best entry points are to check out:

* `inception_zip_file_util`: extracts the relevant XMI files from the ZIP file that INCEpTION provides when you download in the 'UIMA XML/XMI 1.1' format.
* `collection_utils`: You can use the `DocumentCollection` class to read in an entire directory of XMI files into the collection. Next, you can iterate over the CAS objects in this collection.

```
coll = DocumentCollection("some-path")
for doc_name in coll.docs:
    doc = coll.docs[doc_name]
    # Do something with the document

# Serialize collection in case you made any changes.
coll.serialize("output-folder)
```

The `pycas` module provides various methods to access the information in the CAS or to modify it. Also check out the functions provided in the `util` module, in particular if you aim to extract patterns, compare annotations, etc.


## Limitations
* Feature values do not treat other types of ranges, e.g. Integer / Float expliclty, leaving the conversion to primitive types to client code.
* `get_feature_value` does not yet implement feature structure lists. String-based lists are implemented, but have not been extensively tested (and may perform slowly).

