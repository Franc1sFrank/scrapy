import lxml
import parsel
import w3lib
import twisted
import cryptography
import scrapy


class QiushiSpider(scrapy.Spider):
    name = "qiushibaike"

def start_requests(self):
    urls = [
        'https://www.qiushibaike.com/text/page/1/',
        'https://www.qiushibaike.com/text/page/2/',
    ]
    for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        content_left_div = response.xpath('//*[@id="content-left"]')
        content_list_div = content_left_div.xpath('./div')

        for content_div in content_list_div:
            yield {
                'author': content_div.xpath('./div/a[2]/h2/text()').get(),
                'content': content_div.xpath('./a/div/span/text()').getall(),
            }



haders = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36'
    }

def start_requests(self):
    urls = [
        'https://www.qiushibaike.com/text/page/12/',
        'https://www.qiushibaike.com/text/page/2/',
    ]
    for url in urls:
        yield scrapy.Request(url=url, callback=self.parse, headers=self.haders)



content_left_div = response.xpath('//[@id="content-left"]')

content_list_div = content_left_div.xpath('./div')

content_div = content_list_div[0]

author = content_div.xpath('./div/a[2]/h2/text()').get()
print(author)

content = content_div.xpath('./a/div/span/text()').getall()
print(content)

