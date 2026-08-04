"""Immutable broker-neutral data models shared across SCOUT modules."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Literal

OpportunityAction = Literal["avoid", "watch", "research", "prefer"]
SnapshotStatus = Literal["open", "closed", "unknown"]
TradeSide = Literal["buy", "sell", "flat"]
HealthStatus = Literal["ok", "degraded", "down", "unknown"]


@dataclass(frozen=True, slots=True)
class MarketSnapshot:
    """Normalized view of a market instrument at a specific time."""

    symbol: str
    observed_at: datetime
    source: str
    venue: str | None = None
    last_price: Decimal | None = None
    bid_price: Decimal | None = None
    ask_price: Decimal | None = None
    volume: int | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class CandidateTicker:
    """A symbol that has been surfaced for additional review."""

    symbol: str
    score: Decimal
    observed_at: datetime
    rationale: tuple[str, ...] = ()
    metadata: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class TradeSnapshot:
    """Completed trade details mirrored into SCOUT after execution elsewhere."""

    trade_id: str
    symbol: str
    side: TradeSide
    quantity: Decimal
    opened_at: datetime
    closed_at: datetime | None = None
    opened_price: Decimal | None = None
    closed_price: Decimal | None = None
    status: SnapshotStatus = "unknown"
    metadata: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class StrategyRecommendation:
    """Advisory output produced by SCOUT."""

    symbol: str
    action: OpportunityAction
    confidence: Decimal
    generated_at: datetime
    rationale: tuple[str, ...] = ()
    metadata: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class SystemHealth:
    """Health snapshot for a SCOUT subsystem."""

    component: str
    status: HealthStatus
    checked_at: datetime
    details: Mapping[str, str] = field(default_factory=dict)

