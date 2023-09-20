import csv
from datetime import datetime
from collections import defaultdict
from pep_parse.constants import (
    BASE_DIR,
    RESULTS_DIR,
    DATETIME_PATTERN,
    ENCODING,
)


class PepParsePipeline:
    def open_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        suffix = datetime.strftime(datetime.now(), DATETIME_PATTERN)
        self.status_summary_file = open(
            results_dir / f'status_summary_{suffix}.csv',
            'w',
            newline='',
            encoding=ENCODING,
        )
        self.data = defaultdict(int)

    def process_item(self, item, spider):
        self.data[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        writer = csv.writer(self.status_summary_file)
        writer.writerow(('Статус', 'Количество'))
        writer.writerows(self.data.items())
        writer.writerow(('Итого:', sum(self.data.values())))
