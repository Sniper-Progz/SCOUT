"""Tests for the initial SCOUT package layout."""

from __future__ import annotations

from pathlib import Path


def test_expected_module_boundaries_exist() -> None:
    expected = {
        Path("src/scout/runtime"),
        Path("src/scout/configuration"),
        Path("src/scout/logging"),
        Path("src/scout/health_monitoring"),
        Path("src/scout/scanner"),
        Path("src/scout/market_data"),
        Path("src/scout/news"),
        Path("src/scout/catalyst_analysis"),
        Path("src/scout/finbert"),
        Path("src/scout/rss"),
        Path("src/scout/sec"),
        Path("src/scout/analytics"),
        Path("src/scout/replay"),
        Path("src/scout/synchronization"),
        Path("src/scout/historical_database"),
        Path("src/scout/reporting"),
        Path("src/scout/utilities"),
        Path("src/scout/interfaces"),
        Path("src/scout/shared_contracts"),
    }

    for path in expected:
        assert path.is_dir(), path
        assert (path / "__init__.py").is_file(), path

