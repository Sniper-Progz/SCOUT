"""Health monitoring protocol."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from scout.shared_contracts.models import SystemHealth


@runtime_checkable
class HealthMonitor(Protocol):
    """Inspect the health of a SCOUT subsystem."""

    def snapshot(self) -> SystemHealth:
        """Return the current health snapshot."""

