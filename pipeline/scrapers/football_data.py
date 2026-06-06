# football-data.co.uk loader — downloads and parses CSV files for match context data.
import logging
log = logging.getLogger(__name__)


class FootballDataLoader:
    def run(self):
        """Download football-data.co.uk CSVs and load match context into team_seasons table."""
        log.info("FootballDataLoader.run() — stub, not yet implemented")