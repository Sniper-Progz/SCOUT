"""FinBERT sentiment protocol."""

from __future__ import annotations

from decimal import Decimal
from typing import Protocol, runtime_checkable


@runtime_checkable
class FinBertAnalyzer(Protocol):
    """Classify the sentiment of financial text."""

    def score(self, text: str) -> Decimal:
        """Return a deterministic sentiment score for the supplied text."""

