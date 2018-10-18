# -*- coding: utf-8 -*-
import scrapy


class CarrosSpider(scrapy.Spider):
    name = 'carros'
    #allowed_domains = ['https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios']
    start_urls = ['https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/']

    def parse(self, response):
        
        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
        next_page = response.xpath(
            '//div[contains(@class, "module_pagination")]//a[@rel = "next"]/@href'
        )
        if next_page:
            #self.log('Próxima Página: {}'.format(next_page.extract_first()))
            self.log('Próxima Página: %s' % next_page.extract_first())
            yield scrapy.Request(
                url=next_page.extract_first(), callback=self.parse
            )
        
    
    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        year = response.xpath(
            '//span[contains(text(), "Ano")]/following-sibling::strong/a/@title'
        ).extract_first()
        ports = response.xpath(
            '//span[contains(text(), "Portas")]/following-sibling::strong/text()'
        ).extract_first()
        yield {
            'title': title,
            'year': year,
            'ports': ports,
        }
       

