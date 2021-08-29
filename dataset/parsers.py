from enum import Enum
import re

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from dataset.csl import Variable


OPENING_TAGS = re.compile(r"^<(?P<label>{})>(?P<token>.*)".format('|'.join(map(lambda _: _.value, Variable))))
CLOSING_TAGS = re.compile(r"(?P<token>.*)<\/(?P<label>{})>$".format('|'.join(map(lambda _: _.value, Variable))))
ENCLOSED_TAGS = re.compile(r"<(?P<label>{})>(?P<token>.*)<\/\1>".format('|'.join(map(lambda _: _.value, Variable))))

class IOBTag(Enum):
    """An enumeration of `IOB tags <https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)>`_
    """
    INSIDE = 'I'
    OUTSIDE = 'O'
    BEGINNING = 'B'
    SINGLE = 'S'
    END = 'E'

@dataclass
class ParseResult:
    token: str
    tag: Optional[IOBTag] = None
    label: List[str] = field(default_factory=list)

class CSLParser:
    """This class allows the parsing of an annotated string that uses XML-like tags 
    (based on CSL variables) that enclose delimited token(s) using regular expressions.

    Args:
        delimiter (str): delimiter to be used for tokenization. Defaults to whitespace.

    Return:
        CSLParser: A Parser object
    """
    def __init__(self, delimiter: str = ' '):
        self.delimiter = delimiter

    def _tag_token(self, search_results: Dict) -> Optional[IOBTag]:
        if search_results['enclosed']:
            tag = IOBTag.SINGLE
        elif search_results['opening']:
            tag = IOBTag.BEGINNING
        elif search_results['closing']:
            tag = IOBTag.END
        else:
            tag = None
        return tag

    def _parse(self, token: str, result: Optional[ParseResult] = None) -> Dict[str, Any]:
        search_results = {
            'enclosed': ENCLOSED_TAGS.search(token),
            'opening': OPENING_TAGS.search(token),
            'closing': CLOSING_TAGS.search(token)
        }

        tag = self._tag_token(search_results)

        search_result = search_results['enclosed'] or search_results['opening'] or search_results['closing']
                
        if search_result:
            label = Variable(search_result['label'])
            if result: # Nested case
                result.token = search_result['token']
            else:
                result = ParseResult(search_result['token'], tag=tag)
            
            result.label.append(label)
            return self._parse(search_result['token'], result=result)
        else:
            if not result: # Nested case
                return ParseResult(token, tag=tag)

        return result

    def parse(self, s: str) -> List[Tuple[str, str]]:
        """Parse a given string to a list of tuple

        Args:
            s (str): the annotated string to be parsed

        Return:
            List[Tuple[str, str]]: A sequence of tuples; the first element of the tuple is the token and the second element is the label.

            If the token is not enclosed by any tag, it will be labelled as **other**.

            If the token is nested by more than 1 tag, it will be labelled as with period adjoining the labels in hierarchical manner, e.g. **accessed.year**
        """
        results = []

        tag_open = False

        for i, token in enumerate(s.split(self.delimiter)):
            parsed_result = self._parse(token)

            if parsed_result.tag == IOBTag.BEGINNING:
                tag_open = True
            elif parsed_result.tag == IOBTag.END:
                tag_open = False
            elif parsed_result.tag == IOBTag.SINGLE:
                tag_open = False
            
            if not parsed_result.label:
                if tag_open: # No label found and open tag has been found previously
                    parsed_result.label = results[i - 1].label # Use the previous token's label
                else:
                    parsed_result.label.append(Variable.OTHER)

            results.append(parsed_result)

        return [(_.token, ".".join(map(lambda l: l.value, _.label))) for _ in results]