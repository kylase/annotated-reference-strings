# Annotated Reference Strings Dataset

## Introduction

`annotated_reference_strings` dataset consists of millions of reference strings synthesized to _at most 17 CSL styles_ using CSL processor ([`citeproc-js`](https://github.com/Juris-M/citeproc-js)) with the short sequence of tokens (segment) annotated as the variable it is derived from.

This library provide some utility to parse the raw annotated string to a sequence of tuples of token and its label.

For more information on the library and also the dataset, refer to the [documentation](https://kylase.github.io/annotated_reference_strings/).

## Obtaining the dataset

The dataset is prepared in National University of Singapore (NUS), School of Computing (SoC), [Web Information Retrieval / Natural Language Processing Group](https://wing.comp.nus.edu.sg/) as part of Master project.

You can obtain the datasets in partial or full in 2 ways as they are bundled in separated files:

- [NUS SoC's Google Drive (Source of truth)](https://drive.google.com/drive/folders/1xtsdzilLMy7PyfWgbhoPIUJ1YwMX9Qaz?usp=sharing)
- [Hugging Face dataset repository](https://huggingface.co/datasets/yuanchuan/annotated_reference_strings)

If you are downloading from the Google Drive, it will be faster to download them by using [`gdown`](https://github.com/wkentaro/gdown) as Google will zip up the files if you download them through the web interface:

```shell
pip install gdown
gdown <url of the file>
```

If you are using Hugging Face's `datasets` library:

```python
from datasets import load_dataset
dataset = load_dataset('yuanchuan/annotated_reference_strings')
```

## Citing

If you are using the dataset, please cite the following:

```bibtex
@techreport{kee-nus-2021,
    author = {Yuan Chuan Kee},
    title = {Synthesis of a large dataset of annotated reference strings for developing citation parsers},
    institution = {National University of Singapore},
    year = {2021}
}
```
