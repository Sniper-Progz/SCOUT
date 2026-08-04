"""Opportunity scanner protocol."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import CandidateTicker


@runtime_checkable
class Scanner(Protocol):
    """Discover candidate opportunities from upstream signals."""

    def scan(self) -> Sequence[CandidateTicker]:
        """Return ranked candidate tickers."""

