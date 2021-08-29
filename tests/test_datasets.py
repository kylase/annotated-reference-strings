import json
import pytest

from pathlib import Path

from dataset import TextLineDataset
from .fixtures import expected_dataset_file


class TestTextLineDataset:
    def test_instantiate(self, expected_dataset_file: Path):
        dataset = TextLineDataset(expected_dataset_file)

        number_of_lines = 0
        with open(expected_dataset_file) as f:
            for i, _ in enumerate(f):
                line = _.strip()
                if line != "":
                    number_of_lines += 1

                if i == 0:
                    first_line = line

        assert len(dataset) > 0
        assert len(dataset) == number_of_lines
        assert dataset[0] == first_line, f"Zeroth element should be the first line for {expected_dataset_file}"

        assert any(dataset) is True

        with pytest.raises(IndexError):
            dataset[len(dataset)]
