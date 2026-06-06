# WhoScored scraper — headless browser scraper for pre-2014/15 match-level data.
import logging
log = logging.getLogger(__name__)


class WhoScoredScraper:
    def run(self):
        """Scrape WhoScored via Playwright and load raw shots into raw_shots table."""
        log.info("WhoScoredScraper.run() — stub, not yet implemented")