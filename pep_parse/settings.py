from pathlib import Path

BASE_DIR = Path(__file__).parent
RESULTS_DIR = 'results'
(BASE_DIR / RESULTS_DIR).mkdir(exist_ok=True)

DATETIME_PATTERN = '%Y-%m-%dT%H-%M-%S'
ENCODING = 'UTF-8'
SUMMARY_STATUS_COLUMNS = ('Статус', 'Количество')
AMOUNT_STATUSES = 'Итого'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [
    NEWSPIDER_MODULE,
]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}
