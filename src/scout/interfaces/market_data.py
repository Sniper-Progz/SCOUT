"""Market data provider protocol."""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import CandidateTicker, MarketSnapshot


@runtime_checkable
class MarketDataProvider(Protocol):
    """Provide broker-neutral market data access."""

    def get_snapshot(self, symbol: str) -> MarketSnapshot:
        """Return the latest normalized snapshot for a symbol."""

    def list_candidates(self, universe: Iterable[str]) -> Sequence[CandidateTicker]:
        """Return candidate tickers ranked from a supplied universe."""

