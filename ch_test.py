import scrapy


class ChTestSpider(scrapy.Spider):
    name = "ch_test"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/price/brandid_15?pvareaid=104399"]
    #如果网址中http开头，结尾为/，则需要删去/

    def parse(self, response):
        name_list=response.xpath('//div[@class="tw-mb-2 tw-flex tw-flex-wrap tw-items-center"]/a/text()').extract()
        price_list=response.xpath('//div[@class="tw-mb-2.5 tw-flex tw-items-center tw-whitespace-nowrap tw-text-sm tw-text-[#828CA0]"]/a/text()').extract()
        for i in range(len(name_list)):
            name = name_list[i]
            price = price_list[i]
            print(name+'的价格为:'+price)

