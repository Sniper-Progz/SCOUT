"""Future synchronization protocol for versioned SCOUT communication."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import StrategyRecommendation


@runtime_checkable
class SynchronizationService(Protocol):
    """Prepare data for the future SCOUT-to-IVY communication contract."""

    def emit(self, recommendation: StrategyRecommendation) -> None:
        """Emit a versioned synchronization payload."""

