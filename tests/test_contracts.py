"""Tests for broker-neutral shared contracts."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, is_dataclass
from datetime import UTC, datetime
from decimal import Decimal

import pytest

from scout.shared_contracts import (
    CandidateTicker,
    MarketSnapshot,
    StrategyRecommendation,
    SystemHealth,
    TradeSnapshot,
)


def test_contracts_are_immutable_dataclasses() -> None:
    assert is_dataclass(MarketSnapshot)
    assert is_dataclass(CandidateTicker)
    assert is_dataclass(TradeSnapshot)
    assert is_dataclass(StrategyRecommendation)
    assert is_dataclass(SystemHealth)

    snapshot = MarketSnapshot(
        symbol="AAPL",
        observed_at=datetime(2026, 8, 4, tzinfo=UTC),
        source="alpaca",
    )

    with pytest.raises(FrozenInstanceError):
        snapshot.__setattr__("symbol", "MSFT")


def test_contract_instances_can_be_created_without_side_effects() -> None:
    observed_at = datetime(2026, 8, 4, tzinfo=UTC)
    snapshot = MarketSnapshot(
        symbol="AAPL",
        observed_at=observed_at,
        source="alpaca",
    )
    candidate = CandidateTicker(
        symbol="AAPL",
        score=Decimal("0.95"),
        observed_at=observed_at,
    )
    trade = TradeSnapshot(
        trade_id="trade-1",
        symbol="AAPL",
        side="buy",
        quantity=Decimal("10"),
        opened_at=observed_at,
    )
    recommendation = StrategyRecommendation(
        symbol="AAPL",
        action="research",
        confidence=Decimal("0.75"),
        generated_at=observed_at,
    )
    health = SystemHealth(
        component="scanner",
        status="ok",
        checked_at=observed_at,
    )

    assert snapshot.symbol == "AAPL"
    assert candidate.score == Decimal("0.95")
    assert trade.status == "unknown"
    assert recommendation.action == "research"
    assert health.status == "ok"
