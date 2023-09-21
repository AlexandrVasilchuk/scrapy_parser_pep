from re import match

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://{url}/'.format(url=url) for url in allowed_domains]

    def parse(self, response):
        for package in response.css(
            'section#numerical-index tbody > tr a[href*="pep-"]'
        ):
            yield response.follow(package, callback=self.parse_pep)

    def parse_pep(self, response):
        package_name = response.css('section#pep-content h1::text').get()
        yield PepParseItem(
            name=package_name,
            number=match(r'.*?(\d+).*', package_name).group(1),
            status=response.css('dt:contains("Status") + dd ::text').get(),
        )
