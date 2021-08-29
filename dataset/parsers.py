from enum import Enum
import re

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from dataset.csl import Variable


OPENING_TAGS = re.compile(r"^<(?P<label>{})>(?P<token>.*)".format('|'.join(map(lambda _: _.value, Variable))))
CLOSING_TAGS = re.compile(r"(?P<token>.*)<\/(?P<label>{})>$".format('|'.join(map(lambda _: _.value, Variable))))
ENCLOSED_TAGS = re.compile(r"<(?P<label>{})>(?P<token>.*)<\/\1>".format('|'.join(map(lambda _: _.value, Variable))))

class IOBTag(Enum):
    INSIDE = 'I'
    OUTSIDE = 'O'
    BEGINNING = 'B'

@dataclass
class ParseResult:
    token: str
    tag: IOBTag
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

    def _tag(self, parse_results: Dict) -> IOBTag:
        if parse_results['opening']:
            tag = IOBTag.BEGINNING
        elif parse_results['closing']:
            tag = IOBTag.INSIDE
        elif parse_results['enclosed']:
            tag = IOBTag.BEGINNING
        else:
            tag = IOBTag.OUTSIDE
        return tag

    def _parse(self, token: str, result: Optional[ParseResult] = None) -> Dict[str, Any]:
        search_results = {
            'enclosed': ENCLOSED_TAGS.search(token),
            'opening': OPENING_TAGS.search(token),
            'closing': CLOSING_TAGS.search(token)
        }

        tag = self._tag(search_results)

        search_result = search_results['enclosed'] or (search_results['opening'] or search_results['closing'])
        
        if search_result:
            label = Variable(search_result['label'])
            if result:
                result.token = search_result['token']
            else:
                result = ParseResult(search_result['token'], tag=tag)
            
            result.label.append(label)
            return self._parse(search_result['token'], result=result)
        else:
            if not result:
                return ParseResult(token, tag=IOBTag.OUTSIDE)

        return result

    def parse(self, s: str) -> List[Tuple[str, str]]:
        """Parse a given string to a list of tuple

        Args:
            s (str): the annotated string to be parsed

        Return:
            List[Tuple[str, str]]: a sequence of tuples; the first element of the tuple is the token and the second element is the label

            If the token is not enclosed by any tag, it will be labelled as `other`

            If the token is nested by more than 1 tag, it will be labelled as 
        """
        results = []

        for i, token in enumerate(s.split(self.delimiter)):
            parsed_result = self._parse(token)
            
            if not parsed_result.label and parsed_result.tag != IOBTag.OUTSIDE:
                parsed_result.label = results[i - 1].label

            if parsed_result.tag == IOBTag.OUTSIDE:
                parsed_result.label.append(Variable.OTHER)
            results.append(parsed_result)

        return [(_.token, ".".join(map(lambda l: l.value, _.label))) for _ in results]