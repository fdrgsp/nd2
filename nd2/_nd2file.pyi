from typing import Any, List, Sequence, Tuple, overload

import numpy as np
from typing_extensions import Literal

from .structures import Attributes, Coordinate, ExpLoop, FrameMetadata, Metadata

class CND2File:
    path: str
    def __init__(self, path: str) -> None: ...
    def open(self, path: str) -> None: ...
    def close(self) -> None: ...
    def is_open(self) -> bool: ...
    def __enter__(self) -> CND2File: ...
    def __exit__(self, *args: Any) -> bool: ...
    def attributes(self) -> Attributes: ...
    @overload
    def metadata(self, *, format: Literal[True] = ...) -> Metadata: ...
    @overload
    def metadata(self, *, format: Literal[False]) -> dict: ...
    @overload
    def metadata(self, frame: int, *, format: Literal[True] = ...) -> FrameMetadata: ...
    @overload
    def metadata(self, frame: int, *, format: Literal[False]) -> dict: ...
    def experiment(self) -> List[ExpLoop]: ...
    def text_info(self) -> dict: ...
    def seq_count(self) -> int: ...
    def coord_size(self) -> int: ...
    def seq_index_from_coords(self, coords: Sequence[int]) -> int: ...
    def coords_from_seq_index(self, seq_index: int) -> Tuple[int, ...]: ...
    def coord_info(self) -> List[Coordinate]: ...
    def data(self, seq_index: int = 0) -> np.ndarray: ...
    # def image_info(self, seq_index: int = 0) -> structures.ImageInfo: ...
