"""Catalyst analysis protocol."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import StrategyRecommendation


@runtime_checkable
class CatalystAnalyzer(Protocol):
    """Score catalysts from structured market intelligence."""

    def analyze(self, symbol: str, evidence: Sequence[str]) -> StrategyRecommendation:
        """Return a recommendation for a symbol using supporting evidence."""

