"""Reporting protocol."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import StrategyRecommendation


@runtime_checkable
class ReportingService(Protocol):
    """Publish SCOUT advisory output."""

    def publish(self, recommendation: StrategyRecommendation) -> None:
        """Publish a single recommendation."""

