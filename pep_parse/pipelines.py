import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import (
    AMOUNT_STATUSES,
    BASE_DIR,
    DATETIME_PATTERN,
    ENCODING,
    RESULTS_DIR,
    SUMMARY_STATUS_COLUMNS,
)


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.suffix = datetime.strftime(datetime.now(), DATETIME_PATTERN)
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        with open(self.results_dir / f'status_summary_{self.suffix}.csv', 'w', encoding=ENCODING) as file:
            writer = csv.writer(file, dialect=csv.excel, quoting=csv.QUOTE_MINIMAL)
            writer.writerows(
                (
                    SUMMARY_STATUS_COLUMNS,
                    *self.statuses.items(),
                    (AMOUNT_STATUSES, sum(self.statuses.values())),
                )
            )
