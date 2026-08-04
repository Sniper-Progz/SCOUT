"""Structured logging protocol."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol, runtime_checkable


@runtime_checkable
class StructuredLogger(Protocol):
    """Emit structured diagnostic messages."""

    def emit(
        self,
        level: str,
        message: str,
        context: Mapping[str, str] | None = None,
    ) -> None:
        """Write a log event."""
