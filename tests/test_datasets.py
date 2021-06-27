import json
import pytest

from pathlib import Path

from dataset import TextLineDataset

SAMPLE_DATASET_PATH = Path('/Volumes/T3/6_0-final/jstor/en/article/10.2307/annual-reviews.jsonl')


@pytest.fixture(scope="class")
def sample_dataset():
    return SAMPLE_DATASET_PATH

class TestTextLineDataset:
    def test_instantiate(self, sample_dataset):
        dataset = TextLineDataset(sample_dataset)

        number_of_lines = 0
        with open(SAMPLE_DATASET_PATH) as f:
            for i, _ in enumerate(f):
                line = _.strip()
                if line != "":
                    number_of_lines += 1

                if i == 0:
                    first_line = line

        assert len(dataset) > 0
        assert len(dataset) == number_of_lines
        assert dataset[0] == first_line, "Zeroth element should be the first line"

        assert any(dataset) is True

        with pytest.raises(IndexError):
            dataset[len(dataset)]
    
    def test_deserializer(self, sample_dataset):
        dataset = TextLineDataset(sample_dataset, deserializer=json.loads)

        assert any(dataset) is True
        assert type(dataset[0]) != str