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
    def open_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        suffix = datetime.strftime(datetime.now(), DATETIME_PATTERN)
        self.file_name = results_dir / f'status_summary_{suffix}.csv'
        self.amount_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.amount_statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        with open(self.file_name, 'w', encoding=ENCODING, newline='') as file:
            writer = csv.writer(file)
            writer.writerows(
                (
                    SUMMARY_STATUS_COLUMNS,
                    *self.amount_statuses.items(),
                    (AMOUNT_STATUSES, sum(self.amount_statuses.values())),
                )
            )
