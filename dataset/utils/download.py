from pathlib import Path


SAMPLE_MANIFEST_URL = ''
MANIFEST_URL = ''


def download_dataset(path: Path, sample: bool = True):
    """
    A convenient function to download the dataset to specified path

    Args:
        path (Path): The path to save the files to
        sample (bool): Download the sample or the full dataset [default: True; download sample only]
    """
    url = SAMPLE_MANIFEST_URL if sample else MANIFEST_URL


