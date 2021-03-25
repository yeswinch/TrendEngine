import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/gp/site-directory?ref_=nav_em__fullstore_0_1_1_50']

    def parse(self, response):
        items = AmazontutorialItem()

        deptName = response.css('.fsdDeptTitle::text').extract()
        deptImg = response.css('.fsdDeptFullImage::attr(src)').getall()
        cateName = response.css('.fsdDeptLink::text').extract()

        items['deptName'] = deptName
        items['deptImg'] = deptImg
        items['cateName'] = cateName
        
        yield items
 