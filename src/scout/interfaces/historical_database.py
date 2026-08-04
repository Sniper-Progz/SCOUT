"""Historical database protocol."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import MarketSnapshot, TradeSnapshot


@runtime_checkable
class HistoricalDatabase(Protocol):
    """Persist and retrieve historical market intelligence."""

    def store_snapshots(self, snapshots: Sequence[MarketSnapshot]) -> None:
        """Persist market snapshots in chronological order."""

    def store_trades(self, trades: Sequence[TradeSnapshot]) -> None:
        """Persist mirrored completed trade snapshots."""

