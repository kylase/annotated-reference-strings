import csv
import logging
import os
from pathlib import Path
from typing import Optional

MANIFEST = "manifest.csv"
GOOGLE_DRIVE_URL_TEMPLATE = "https://drive.google.com/uc?id={}"


def download_dataset(path: Optional[Path] = None, sample: bool = True):
    """
    A convenient function to download the dataset to specified path

    Args:
        path (Path): The path to save the files to [default is to use Path.cwd()/.data]
        sample (bool): Download the sample or the full dataset [default: True; download sample only]
    """
    try:
        import gdown
    except ImportError:
        logging.debug("It is intentional to not make `gdown` a dependency.")
        raise ImportError("You need `gdown` to download the full dataset.")

    with open(MANIFEST) as f:
        reader = csv.reader(f)

        cache_dir = path or os.getenv("CACHE_DIR", Path.cwd() / ".data")
        if not cache_dir.exists():
            logging.info("%s doesn't exist, it will be created.", cache_dir)
            os.makedirs(cache_dir)

        logging.info("Downloading files to %s", cache_dir)

        for filename, google_drive_id in reader:
            output_file = cache_dir / filename

            if not output_file.exists():
                gdown.download(
                    GOOGLE_DRIVE_URL_TEMPLATE.format(google_drive_id),
                    str(output_file),
                )
            else:
                logging.info("%s already exist", output_file)
