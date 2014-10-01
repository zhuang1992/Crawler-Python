from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mobile.items import ReviewItem
class TripCrawler(CrawlSpider):

    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['http://www.tripadvisor.com/Restaurants-g53449-Pittsburgh_Pennsylvania.html']
    rules = [Rule(LinkExtractor(allow=['/Restaurant_Review[-_A-Za-z0-9]*\.html']), 'parse_restaurant')]

    def parse_restaurant(self, response):
        review = ReviewItem()
        review['url'] = response.url
        review['restaurant'] = "abcdefg"
        review['review'] = "response.xpath()"
        review['rate'] = response.xpath("//div[@id='description']/text()[position() > 1 and position()<last()]").extract()
        review['user'] = response.xpath("//div[@id='specifications']/p[2]/text()[2]").extract()
        return review