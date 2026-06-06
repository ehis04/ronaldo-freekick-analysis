# Ronaldo Free Kick Analysis — master pipeline entry point.
# Run with: python run_pipeline.py [--phase PHASE] [--skip-scrape] [--skip-process] [--skip-analysis] [--skip-export]

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.config.settings import LOG_LEVEL, PIPELINE_ENV, ensure_output_dirs
from pipeline.db.schema import create_all_tables
from pipeline.db.connection import get_connection


logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("pipeline")


def parse_args():
    parser = argparse.ArgumentParser(description="Ronaldo free kick analysis pipeline")
    parser.add_argument("--skip-scrape",   action="store_true")
    parser.add_argument("--skip-process",  action="store_true")
    parser.add_argument("--skip-analysis", action="store_true")
    parser.add_argument("--skip-export",   action="store_true")
    return parser.parse_args()


def run_scrapers():
    """Invoke all source scrapers and load raw data into DuckDB."""
    log.info("Phase: scrapers")
    from pipeline.scrapers.understat  import UnderstatScraper
    from pipeline.scrapers.fbref      import FBRefScraper
    from pipeline.scrapers.whoscored  import WhoScoredScraper
    from pipeline.scrapers.sofascore  import SofaScoreScraper
    from pipeline.scrapers.transfermarkt import TransfermarktScraper
    from pipeline.scrapers.statsbomb  import StatsBombLoader
    from pipeline.scrapers.football_data import FootballDataLoader

    for scraper_cls in [
        UnderstatScraper,
        FBRefScraper,
        WhoScoredScraper,
        SofaScoreScraper,
        TransfermarktScraper,
        StatsBombLoader,
        FootballDataLoader,
    ]:
        log.info(f"  Running {scraper_cls.__name__}")
        scraper_cls().run()


def run_processors():
    """Clean, enrich, and deduplicate raw shots into processed_shots."""
    log.info("Phase: processors")
    from pipeline.processors.shot_cleaner    import ShotCleaner
    from pipeline.processors.zone_classifier import ZoneClassifier
    from pipeline.processors.phase_tagger   import PhaseTagger
    from pipeline.processors.technique_tagger import TechniqueTagger
    from pipeline.processors.context_builder  import ContextBuilder
    from pipeline.processors.xg_normaliser    import XGNormaliser

    for processor_cls in [
        ShotCleaner,
        ZoneClassifier,
        PhaseTagger,
        TechniqueTagger,
        ContextBuilder,
        XGNormaliser,
    ]:
        log.info(f"  Running {processor_cls.__name__}")
        processor_cls().run()


def run_analysis():
    """Compute all metrics from processed_shots."""
    log.info("Phase: analysis")
    from pipeline.analysis.conversion      import ConversionAnalyser
    from pipeline.analysis.shot_quality    import ShotQualityAnalyser
    from pipeline.analysis.delivery        import DeliveryAnalyser
    from pipeline.analysis.peer_comparison import PeerComparisonAnalyser
    from pipeline.analysis.team_impact     import TeamImpactAnalyser
    from pipeline.analysis.context_analysis import ContextAnalyser
    from pipeline.analysis.career_arc      import CareerArcAnalyser
    from pipeline.analysis.output_share    import OutputShareAnalyser

    for analyser_cls in [
        ConversionAnalyser,
        ShotQualityAnalyser,
        DeliveryAnalyser,
        PeerComparisonAnalyser,
        TeamImpactAnalyser,
        ContextAnalyser,
        CareerArcAnalyser,
        OutputShareAnalyser,
    ]:
        log.info(f"  Running {analyser_cls.__name__}")
        analyser_cls().run()


def run_exporters():
    """Write all JSON files to the frontend data directory."""
    log.info("Phase: exporters")
    from pipeline.exporters.data_exporter   import DataExporter
    from pipeline.exporters.config_exporter import ConfigExporter

    for exporter_cls in [ConfigExporter, DataExporter]:
        log.info(f"  Running {exporter_cls.__name__}")
        exporter_cls().run()


def main():
    args = parse_args()
    log.info(f"Pipeline starting — env: {PIPELINE_ENV}")

    ensure_output_dirs()

    conn = get_connection()
    create_all_tables(conn)
    conn.close()
    log.info("Database schema ready")

    if not args.skip_scrape:
        run_scrapers()

    if not args.skip_process:
        run_processors()

    if not args.skip_analysis:
        run_analysis()

    if not args.skip_export:
        run_exporters()

    log.info("Pipeline complete")


if __name__ == "__main__":
    main()