# Data exporter — queries DuckDB and writes all data JSON files for the frontend.
import logging
log = logging.getLogger(__name__)


class DataExporter:
    def run(self):
        """Write shots, seasons, zones, peers, team_impact, context, career_arc, delivery, international, output_share JSON."""
        log.info("DataExporter.run() — stub, not yet implemented")