"""Reserved Alpaca market data adapter boundary.

Higher-level modules must depend on :mod:`scout.interfaces.market_data`, not on
this provider module directly.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AlpacaMarketDataSettings:
    """Configuration for a future Alpaca adapter."""

    base_url: str
    api_key_id: str
    api_secret_key: str

