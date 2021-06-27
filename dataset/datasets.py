import logging
from itertools import islice
from linecache import getline
from pathlib import Path
from typing import Callable, Optional, Sequence, Tuple, Union

from torch.utils.data import Dataset


class TextLineDataset(Dataset):
    """Read a text-based file with a given encoding and deserialise each line with deserializer (if provided).

    Args:
        file_path (Union[Path, str]): The path of the text file
        encoding (str, optional): The encoding of the file. Defaults to "utf-8".
        lazy_load (bool, optional): Use lazy loading. Defaults to :py:obj:`False`.
        deserializer (Callable[[str], Sequence[Tuple[str, str]]]): A callable that takes the line and return a deserialised form. If :py:const:`None`, it will be str

    Raise:
        FileNotFoundError: If :py:data:`file_path` does not exist
        IndexError: If index of the dataset is more than the :py:meth:`len` - 1
    
    Return:
        TextLineDataset: A dataset object
    
    Attributes:
        root (Union[Path, str]): The path of the text file
        encoding (str): The encoding of the text file
        lazy_load (bool): Whether to lazy load the line when :py:meth:`__getitem__` is called, otherwise use :py:mod:`linecache  <https://docs.python.org/3/library/linecache.html>`
        deserializer (Callable[[str], Sequence[Tuple[str, str]]]]): A function to deserialise each line
    """
    def __init__(self, file_path: Union[Path, str], encoding: str = 'utf-8', lazy_load: bool = False,
                 deserializer: Optional[Callable[[str], Sequence[Tuple[str, str]]]] = None):
        if isinstance(file_path, str):
            file_path = Path(file_path)

        if not file_path.exists():
            logging.error("%s cannot be found.", file_path)
            raise FileNotFoundError(f"{file_path} not found.")
        else:
            self.encoding = encoding
            self.root = file_path
            self._len = 0

            with self.root.open(encoding=self.encoding) as fh:
                for _ in fh:
                    line = _.strip()
                    if line != "":
                        self._len += 1

        self.lazy_load = lazy_load
        self.deserializer = deserializer

    def _get_line(self, line_no: int) -> str:
        assert line_no > 0, "line_no must be a positive integer"
        if self.lazy_load:
            with self.root.open(encoding=self.encoding) as fh:
                line = list(islice(fh, line_no - 1, line_no))[0]
        else:
            line = getline(str(self.root.absolute()), line_no)

        return line.strip()

    def __len__(self):
        return self._len

    def __getitem__(self, item: int) -> Union[str, Sequence[Tuple[str, str]]]:
        line_no = item + 1

        if line_no >= len(self):
            raise IndexError(f"Index {item} out-of-bound")

        if self.deserializer:
            return self.deserializer(self._get_line(line_no))
        return self._get_line(line_no)
