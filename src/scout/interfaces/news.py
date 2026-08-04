"""News provider protocol."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable


@runtime_checkable
class NewsProvider(Protocol):
    """Provide normalized news content for downstream analysis."""

    def headlines(self, symbol: str) -> Sequence[str]:
        """Return a stable sequence of headlines for a symbol."""

