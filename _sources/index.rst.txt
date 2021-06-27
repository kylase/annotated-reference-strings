Reference Strings Dataset
=========================

Quick Introduction
------------------

*Reference Strings Dataset* is a collection of synthetically generated bibliographies that comes with annotations on each token. For example, a citation rendered in *APA* style:

.. code-block:: 
   :caption: Plain text render of a citation
   :name: plain-text-render

   Watson, J. D., & Crick, F. H. C. (1953). Molecular structure of nucleic acids: A structure for deoxyribose nucleic acid. Nature, 171(4356), 737–738. https://doi.org/10.1038/171737a0

The corresponding annotated form encloses contigious segment of tokens with :abbr:`XML (Extensible Markup Language)`-like tags:

.. code-block:: 
   :caption: Plain text render of a citation with annotation
   :name: plain-text-render-with-annotation

   <author>Watson, J. D., & Crick, F. H. C.</author> <year>(1953).</year> <title>Molecular structure of nucleic acids: A structure for deoxyribose nucleic acid.</title> <container-title>Nature,</container-title> <volume>171</volume> <issue>(4356),</issue> <page>737–738.</page> <DOI>https://doi.org/10.1038/171737a0</DOI>

These XML-like tags are based on :abbr:`CSL (Citation Style Language)` `Variables <https://docs.citationstyles.org/en/stable/specification.html#appendix-iv-variables>`_.

For more information about the method which the dataset is synthesized and the data format, read :doc:`details/index`.

Use Cases
^^^^^^^^^

Sequence tagging/labeling
   Assignment of categorical label to each member of the sequence.

How to obtain the dataset
-------------------------

Visit the :doc:`obtaining-data/downloads` page for instructions.

Citing
------

This dataset is part of a Master project in NUS.

If you are using the dataset for scientific work, please cite the following:

.. literalinclude:: ../citation.bib
   :language: bibtex

Content
-------

.. toctree::
   :maxdepth: 2

   usage/requirements
   details/index
   obtaining-data/downloads
   references/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
