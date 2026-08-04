"""Analytics pipeline protocol."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import MarketSnapshot, StrategyRecommendation


@runtime_checkable
class AnalyticsEngine(Protocol):
    """Build derived intelligence from historical market snapshots."""

    def build(
        self,
        snapshots: Sequence[MarketSnapshot],
    ) -> Sequence[StrategyRecommendation]:
        """Produce recommendation candidates from normalized snapshots."""
