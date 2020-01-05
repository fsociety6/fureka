import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class QuotesSpider(scrapy.Spider):
    name = "pests"

    def start_requests(self):
        urls = [
            'http://127.0.0.1:8080/pest.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        links=response.xpath('//app-filter-result/div/a/@href')
        for link in links:
            next_page = link.get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.follow_link)
            # yield {
            #     'name':name.xpath('.//div/div[2]/h2/text()').extract_first(),
            #     'scientific_name':name.xpath('.//div/div[2]/p/i/text()').extract_first(),
            #     'url': name.xpath('.//@href').extract_first(),
            #     'type':name.xpath('.//div/div[2]/div[1]/p/text()').extract_first(),
            # }
    def follow_link(self,response):
        yield {
            'name':response.xpath('//*[@id="overview"]/h3[1]/text()').extract_first(),
            'scientific_name':response.xpath('//*[@id="overview"]/p/i/text()').extract_first(),
            'type':response.xpath('//*[@id="overview"]/div[1]/p/text()').extract_first(),
            'symptoms':response.xpath('//*[@id="pathogen-detail-wrapper"]/div[3]/div/div[2]/div[1]/p/text()').extract_first(),
            'hosts':response.xpath('//*[@id="overview"]/div[2]/div/p/text()').getall(),
            'trigger':response.xpath('//*[@id="pathogen-detail-wrapper"]/div[3]/div/div[2]/div[2]/p/text()').get(),
            'biaological_control':response.xpath('//*[@id="pathogen-detail-wrapper"]/div[3]/div/div[2]/div[3]/p/text()').get(),
            'chemical_control':response.xpath('//*[@id="pathogen-detail-wrapper"]/div[3]/div/div[2]/div[4]/p/text()').get(),
            'preventive_measures':response.xpath('//*[@id="pathogen-detail-wrapper"]/div[3]/div/div[2]/div[5]/ul/li/text()').getall(),
            'images':response.xpath('//*[@id="pathogen-detail-wrapper"]/div[2]/app-pathogen-images-carousel/div/div/div/img/@src').getall(),
        }