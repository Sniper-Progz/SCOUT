"""Tests for SCOUT protocol boundaries."""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from datetime import UTC, datetime
from decimal import Decimal

from scout.interfaces import MarketDataProvider, Scanner, StructuredLogger
from scout.shared_contracts import CandidateTicker, MarketSnapshot


class _MarketDataProvider:
    def get_snapshot(self, symbol: str) -> MarketSnapshot:
        return MarketSnapshot(
            symbol=symbol,
            observed_at=datetime(2026, 8, 4, tzinfo=UTC),
            source="test",
        )

    def list_candidates(self, universe: Iterable[str]) -> Sequence[CandidateTicker]:
        observed_at = datetime(2026, 8, 4, tzinfo=UTC)
        return [
            CandidateTicker(
                symbol=symbol,
                score=Decimal("1"),
                observed_at=observed_at,
            )
            for symbol in universe
        ]


class _Scanner:
    def scan(self) -> Sequence[CandidateTicker]:
        observed_at = datetime(2026, 8, 4, tzinfo=UTC)
        return [
            CandidateTicker(symbol="AAPL", score=Decimal("1"), observed_at=observed_at)
        ]


class _Logger:
    def emit(
        self,
        level: str,
        message: str,
        context: dict[str, str] | None = None,
    ) -> None:
        _ = level, message, context


def test_protocols_are_runtime_checkable() -> None:
    provider = _MarketDataProvider()
    scanner = _Scanner()
    logger = _Logger()

    assert isinstance(provider, MarketDataProvider)
    assert isinstance(scanner, Scanner)
    assert isinstance(logger, StructuredLogger)
