# -*- coding: utf-8 -*-
import scrapy


class CarrosSpider(scrapy.Spider):
    name = 'carros'
    #allowed_domains = ['https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios']
    start_urls = ['https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/']

    def parse(self, response):
        items = response.xpath(
            '//ul[@id="main-ad-list"]/li'
        )
        for item in items:
            self.log(item.xpath('./a/@href').extract_first())
            
