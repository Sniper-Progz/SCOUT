"""SEC ingestion protocol."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable


@runtime_checkable
class SecFilingReader(Protocol):
    """Read and normalize SEC filing content."""

    def filings(self, symbol: str) -> Sequence[str]:
        """Return stable text snippets from the SEC feed."""

