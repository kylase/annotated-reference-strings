Details
=======

This page describe how the dataset is derived and the description of it.

Data Sources
------------

The citations are obtained from the following sources:

#. CrossRef via :abbr:`DOI (Document Object Identifier)` obtained from `Open Academic Graph <https://www.microsoft.com/en-us/research/project/open-academic-graph/>`_
#. JSTOR Sample Dataset (not accessible anymore)
#. `PubMed (2019 Baseline) <https://www.nlm.nih.gov/databases/download/pubmed_medline.html>`_

CSL Styles
----------

In total, 17 styles have been employed. The table below summarises the number of reference strings available in the dataset for each style.

.. csv-table:: Number of Strings By CSL Style
   :file: ../stats/csl-styles-strings-count.csv
   :widths: 50, 80
   :header-rows: 1


BibTeX Entry Types
------------------

The table below summarises the number of reference strings available for each BibTeX entry type.

.. csv-table:: Number of Strings By BibTeX Entry Types
   :file: ../stats/bibtex-entry-types-strings-count.csv
   :widths: 50, 80
   :header-rows: 1

Data Format
-----------

The data are stored as JSON lines in each file. Each line of the files represents a citation rendered in a specified CSL style with its corresponding annotated sequence.

.. code-block:: json
   :caption: An example (annotated by segment) with its metadata such as the source, document type and the style the citation is rendered

   {
      "style": "apa",
      "doc_type": "article",
      "source": "crossref",
      "data": "<author>Watson, J. D., & Crick, F. H. C.</author> <year>(1953).</year> <title>Molecular structure of nucleic acids: A structure for deoxyribose nucleic acid.</title> <container-title>Nature,</container-title> <volume>171</volume> <issue>(4356),</issue> <page>737\\u2013738.</page> <DOI>https://doi.org/10.1038/171737a0</DOI>"
   }

.. important:: Not all tokens are enclosed within the tags. These should be labelled as **O** (according to tagging scheme).
