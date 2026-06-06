# Shot cleaner — deduplicates and standardises raw_shots into processed_shots.
import logging
log = logging.getLogger(__name__)


class ShotCleaner:
    def run(self):
        """Deduplicate raw_shots across sources and write cleaned rows to processed_shots."""
        log.info("ShotCleaner.run() — stub, not yet implemented")