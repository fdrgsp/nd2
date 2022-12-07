from __future__ import annotations

from pathlib import Path
from typing import Any, Sequence

import numpy as np
from nd2 import structures

class ND2Reader:
    path: str
    _meta_map: dict[str, int]  # map of metadata keys to their byte offset
    _frame_map: dict[int, int]  # map of sequence index to byte offset

    def __init__(
        self,
        path: str | Path,
        validate_frames: bool = False,
        search_window: int = 100,
        read_using_sdk: bool | None = None,
    ) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> ND2Reader: ...
    def __exit__(self, *args) -> None: ...
    def _attributes(self) -> dict: ...
    @property
    def attributes(self) -> structures.Attributes: ...
    def _metadata(self) -> dict: ...
    def metadata(self) -> structures.Metadata: ...
    def _frame_metadata(self, seq_index: int) -> dict: ...
    def frame_metadata(self, seq_index: int) -> structures.FrameMetadata: ...
    def text_info(self) -> dict[str, Any]: ...
    def _description(self) -> str: ...
    def _experiment(self) -> list: ...
    def experiment(self) -> list[structures.ExpLoop]: ...
    def sizes(self) -> dict: ...
    def _seq_count(self) -> int: ...
    def _coord_size(self) -> int: ...
    def _seq_index_from_coords(self, coords: Sequence) -> int: ...
    def _coords_from_seq_index(self, seq_index: int) -> tuple[int, ...]: ...
    def _seq_index_from_pycoords(self, coords: Sequence) -> int: ...
    def _pycoords_from_seq_index(self, seq_index: int) -> tuple[int, ...]: ...
    def _coord_info(self) -> list[tuple[int, str, int]]: ...
    def _image(self, seq_index: int) -> np.ndarray: ...
    def voxel_size(self) -> tuple[float, float, float]: ...
    def _custom_data(self) -> dict[str, Any]: ...
    def _read_image(self, index: int) -> np.ndarray: ...
    def channel_names(self) -> list[str]: ...
    def _get_meta_chunk(self, key: str) -> bytes:
        """Return the metadata chunk for the given key in `_meta_map`."""
