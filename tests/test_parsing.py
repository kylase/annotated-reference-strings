from typing import List

from dataset.csl import Variable
from dataset.parsers import CLOSING_TAGS, ENCLOSED_TAGS, OPENING_TAGS, Parser
from hypothesis import given
from hypothesis.strategies import text

from tests.strategies import (alphanumerics, flat_close_tags,
                              flat_enclosed_tags, flat_open_tags,
                              nested_close_tags, nested_enclosed_tags,
                              nested_open_tags, single_flat_tagged_sequence)


class TestOpeningTagsRegex:
    @given(flat_open_tags())
    def test_search_flat_tags(self, token: str):
        result = OPENING_TAGS.search(token)

        assert result is not None
        assert f"<{result['label']}>{result['token']}" == token

    @given(nested_open_tags())
    def test_search_nested_tags(self, token: str):
        result = OPENING_TAGS.search(token)

        assert result is not None
        assert f"<{result['label']}>{result['token']}" == token

        nested_result = OPENING_TAGS.search(result['token'])

        assert nested_result is not None
        assert result['token'] == f"<{nested_result['label']}>{nested_result['token']}"

    @given(text(alphanumerics, min_size=1))
    def test_search_tagless(self, token: str):
        result = OPENING_TAGS.search(token)

        assert result is None


class TestClosingTagsRegex:
    @given(flat_close_tags())
    def test_search_flat_tags(self, token: str):
        result = CLOSING_TAGS.search(token)

        assert result is not None
        assert f"{result['token']}</{result['label']}>" == token

    @given(nested_close_tags())
    def test_search_nested_tags(self, token: str):
        result = CLOSING_TAGS.search(token)

        assert result is not None
        assert f"{result['token']}</{result['label']}>" == token

        nested_result = CLOSING_TAGS.search(result['token'])

        assert nested_result is not None
        assert result['token'] == f"{nested_result['token']}</{nested_result['label']}>"

    @given(text(alphanumerics, min_size=1))
    def test_search_tagless(self, token: str):
        result = CLOSING_TAGS.search(token)

        assert result is None


class TestEnclosedTagsRegex:
    @given(flat_enclosed_tags())
    def test_search_flat_tags(self, token: str):
        result = ENCLOSED_TAGS.search(token)

        assert result is not None
        assert f"<{result['label']}>{result['token']}</{result['label']}>" == token

    @given(nested_enclosed_tags())
    def test_search_nested_tags(self, token: str):
        result = ENCLOSED_TAGS.search(token)

        assert result is not None
        assert f"<{result['label']}>{result['token']}</{result['label']}>" == token

        nested_result = ENCLOSED_TAGS.search(result['token'])

        assert nested_result is not None
        assert result['token'] == f"<{nested_result['label']}>{nested_result['token']}</{nested_result['label']}>"

    @given(text(alphanumerics, min_size=1))
    def test_search_tagless(self, token: str):
        result = ENCLOSED_TAGS.search(token)

        assert result is None


class TestParser:
    @given(single_flat_tagged_sequence())
    def test_single_tag(self, sequence: List[str]):
        parser = Parser()
        result = parser.parse(sequence)

        for token, label in result:
            assert token is not None
            assert label is not None
            assert label in set(map(lambda _: _.value, Variable))
