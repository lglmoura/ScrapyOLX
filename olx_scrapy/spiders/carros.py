# -*- coding: utf-8 -*-
import scrapy


class CarrosSpider(scrapy.Spider):
    name = 'carros'
    allowed_domains = ['https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios']
    start_urls = ['http://https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/']

    def parse(self, response):
        pass
