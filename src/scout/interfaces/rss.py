"""RSS ingestion protocol."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable


@runtime_checkable
class RssFeedReader(Protocol):
    """Read and normalize RSS feed content."""

    def read(self, url: str) -> Sequence[str]:
        """Return stable text entries from an RSS feed."""

