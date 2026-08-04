"""Utility protocol definitions."""

from __future__ import annotations

from datetime import datetime
from typing import Protocol, runtime_checkable


@runtime_checkable
class Clock(Protocol):
    """Provide the current time through dependency injection."""

    def now(self) -> datetime:
        """Return the current time."""

