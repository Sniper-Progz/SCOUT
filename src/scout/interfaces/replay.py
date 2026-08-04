"""Completed-trade replay protocol."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import StrategyRecommendation, TradeSnapshot


@runtime_checkable
class ReplayEngine(Protocol):
    """Mirror completed trade snapshots into advisory outputs."""

    def replay(
        self,
        trades: Sequence[TradeSnapshot],
    ) -> Sequence[StrategyRecommendation]:
        """Convert completed trades into recommendations or reports."""
