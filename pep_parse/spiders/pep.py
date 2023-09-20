import scrapy
from re import match
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_packages = response.css(
            'section#numerical-index tbody > tr a[href*="pep-"]'
        )
        for package in pep_packages:
            yield response.follow(package, callback=self.parse_pep)

    def parse_pep(self, response):
        yield PepParseItem(
            {
                'name': response.css('section#pep-content h1::text').get(),
                'number': match(
                    r'.*?(\d+).*',
                    response.css('section#pep-content h1::text').get(),
                ).group(1),
                'status': response.xpath(
                    '//dt[contains(., "Status")]'
                    '//following-sibling::dd//text()'
                ).get(),
            }
        )
