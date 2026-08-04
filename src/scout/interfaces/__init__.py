"""Service protocols that define SCOUT boundaries."""

from scout.interfaces.analytics import AnalyticsEngine
from scout.interfaces.catalyst_analysis import CatalystAnalyzer
from scout.interfaces.configuration import ConfigurationSource
from scout.interfaces.finbert import FinBertAnalyzer
from scout.interfaces.health_monitoring import HealthMonitor
from scout.interfaces.historical_database import HistoricalDatabase
from scout.interfaces.logging import StructuredLogger
from scout.interfaces.market_data import MarketDataProvider
from scout.interfaces.news import NewsProvider
from scout.interfaces.replay import ReplayEngine
from scout.interfaces.reporting import ReportingService
from scout.interfaces.rss import RssFeedReader
from scout.interfaces.runtime import RuntimeService
from scout.interfaces.scanner import Scanner
from scout.interfaces.sec import SecFilingReader
from scout.interfaces.synchronization import SynchronizationService
from scout.interfaces.utilities import Clock

__all__ = [
    "AnalyticsEngine",
    "CatalystAnalyzer",
    "Clock",
    "ConfigurationSource",
    "FinBertAnalyzer",
    "HealthMonitor",
    "HistoricalDatabase",
    "MarketDataProvider",
    "NewsProvider",
    "ReplayEngine",
    "ReportingService",
    "RssFeedReader",
    "RuntimeService",
    "Scanner",
    "SecFilingReader",
    "StructuredLogger",
    "SynchronizationService",
]
