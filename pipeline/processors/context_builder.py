# Context builder — reconstructs scoreline state and game context tags for each shot.
import logging
log = logging.getLogger(__name__)


class ContextBuilder:
    def run(self):
        """Set scoreline_state, score_diff, minute_bucket, and match_importance on processed_shots."""
        log.info("ContextBuilder.run() — stub, not yet implemented")