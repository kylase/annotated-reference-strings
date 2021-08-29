from pathlib import Path

import pytest

fixture_path = Path('tests/fixtures')

datasets_path = fixture_path / 'dataset'


@pytest.fixture(
    params=list(datasets_path.glob("en/**/expected.txt")),
    ids=map(lambda path: "/".join(path.split('/')[-4:-1]), map(str, list(datasets_path.glob("en/**/expected.txt")))),
    scope="class"
)
def expected_dataset_file(request):
    return request.param