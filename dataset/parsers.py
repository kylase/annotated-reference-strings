import re

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from dataset.csl import Variable


OPENING_TAGS = re.compile(r"^<(?P<label>{})>(?P<token>.*)".format('|'.join(map(lambda _: _.value, Variable))))
CLOSING_TAGS = re.compile(r"(?P<token>.*)<\/(?P<label>{})>$".format('|'.join(map(lambda _: _.value, Variable))))
ENCLOSED_TAGS = re.compile(r"<(?P<label>{})>(?P<token>.*)<\/\1>".format('|'.join(map(lambda _: _.value, Variable))))

@dataclass
class ParseResult:
    token: str
    label: List[str] = field(default_factory=list)

class Parser:
    def __init__(self, delimiter: str = ' '):
        self.delimiter = delimiter

    def _parse(self, token: str, result: Optional[ParseResult] = None) -> Dict[str, Any]:
        search_result = ENCLOSED_TAGS.search(token) or (OPENING_TAGS.search(token) or CLOSING_TAGS.search(token))
        
        if search_result:
            label = search_result['label']
            if result:
                result.token = search_result['token']
            else:
                result = ParseResult(search_result['token'])
            
            result.label.append(label)
            return self._parse(search_result['token'], result=result)
        else:
            if not result:
                return ParseResult(token)

        return result

    def parse(self, s: str) -> List[Tuple[str, str]]:
        results = []

        for i, token in enumerate(s.split(self.delimiter)):
            parsed_result = self._parse(token)

            if not parsed_result.label:
                parsed_result.label = results[i - 1].label
            results.append(parsed_result)

        return [(_.token, ".".join(_.label)) for _ in results]