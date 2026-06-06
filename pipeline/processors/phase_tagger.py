# Phase tagger — assigns career phase to each shot based on match date.
import logging
log = logging.getLogger(__name__)


class PhaseTagger:
    def run(self):
        """Set phase_id and phase_label on all processed_shots rows using match_date."""
        log.info("PhaseTagger.run() — stub, not yet implemented")