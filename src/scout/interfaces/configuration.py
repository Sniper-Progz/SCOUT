"""Configuration access protocol."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class ConfigurationSource(Protocol):
    """Provide typed access to runtime configuration values."""

    def get(self, key: str) -> str | None:
        """Return the configured value for a key, or ``None`` if absent."""

