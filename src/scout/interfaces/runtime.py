"""Runtime orchestration protocol."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class RuntimeService(Protocol):
    """Coordinate SCOUT lifecycle operations."""

    def run(self) -> None:
        """Start the runtime loop."""

