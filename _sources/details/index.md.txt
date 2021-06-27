# Details

This page describe how the dataset is derived and the description of it.

## Data Sources

The citations are obtained from the following sources:

1. CrossRef via {abbr}`DOI (Document Object Identifier)` obtained from [Open Academic Graph](https://www.microsoft.com/en-us/research/project/open-academic-graph/)
1. JSTOR Sample Dataset (not accessible anymore)
1. [PubMed (2019 Baseline)](https://www.nlm.nih.gov/databases/download/pubmed_medline.html)

## CSL Styles

In total, 17 styles have been employed. The table below summarises the number of reference strings available in the dataset for each style.

Style | Number of Reference Strings
----- | ---------------------------
Annual Reviews | placeholder
APA 6th edition | placeholder
Cambridge University Press | placeholder
Chicago | placeholder
Current Opinion | placeholder
Elsevier (Harvard) | placeholder
Elsevier (Vancouver) | placeholder
IEEE | placeholder
MLA 7th edition | placeholder
Nature | placeholder
University of New South Wales (Oxford) | placeholder
Springer Humanities | placeholder
Springer MathPhys | placeholder
Springer (Vancouver) | placeholder
Taylor and Francis (Harvard) | placeholder
Wiley-VCH Books | placeholder

## BibTeX Entry Types

The table below summarises the number of reference strings available for each BibTeX entry type.

Entry Type | Number of Reference Strings
---------- | ---------------------------
article | placeholder
book | placeholder
inbook | placeholder
incollection | placeholder
inproceedings | placeholder
misc | placeholder
phdthesis | placeholder
techreport | placeholder

## Data Format

There are 2 format which the dataset is stored as: 1) [annotated sequences (by segment) in XML-like tags](#annotated-sequence-by-segment) and 2) [annotated sequences (by token)](#annotated-sequence-by-token).

The data are stored as JSON lines in each file. Each line of the files represents a citation rendered in a specified CSL style with its corresponding annotated sequence.

(annotated_sequence_by_segment)=

### Annotated Sequence (by segment)

```{code-block} json
---
caption: An example (annotated by segment) with its metadata such as the source, document type and the style the citation is rendered
---
{
    "style": "apa",
    "doc_type": "article",
    "source": "crossref",
    "data": "<author>Watson, J. D., & Crick, F. H. C.</author> <year>(1953).</year> <title>Molecular structure of nucleic acids: A structure for deoxyribose nucleic acid.</title> <container-title>Nature,</container-title> <volume>171</volume> <issue>(4356),</issue> <page>737\\u2013738.</page> <DOI>https://doi.org/10.1038/171737a0</DOI>"
}
```

(annotated_sequence_by_token)=

### Annotated Sequence (by token)

```{important} This is derived from the above using regular expression.
```

```{code-block} json
---
caption: An example (annotated by token) with its metadata such as the source, document type and the style the citation is rendered
---
{
    "style": "apa",
    "doc_type": "article",
    "source": "crossref",
    "data": [
        ["Watson,", "author"],
        ["J.", "author"],
        ["D.,", "author"],
        ["&", "author"],
        ["Crick,", "author"],
        ["F.", "author"],
        ["H.", "author"],
        ["C.", "author"],
        ["(1953).", "year"],
        ["Molecular", "title"],
        ["structure", "title"],
        ["of", "title"],
        ["nucleic", "title"],
        ["acids:", "title"],
        ["A", "title"],
        ["structure", "title"],
        ["for", "title"],
        ["deoxyribose", "title"],
        ["nucleic", "title"],
        ["acid.", "title"],
        ["Nature,", "container-title"],
        ["171", "volume"],
        ["(4356),", "issue"],
        ["737\\u2013738.", "page"],
        ["https://doi.org/10.1038/171737a0", "DOI"]
    ]
}
```
