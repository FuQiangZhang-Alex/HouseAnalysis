import scrapy
import logging
import regex
from urllib.parse import urlparse
from json import JSONDecoder


class soufang_spider(scrapy.Spider):

    name = 'lianjia'

    def start_requests(self):
        urls = [
            'http://cd.fang.lianjia.com/loupan/',
            'http://bj.fang.lianjia.com/loupan/',
            'http://nj.fang.lianjia.com/loupan/',
            'http://cq.fang.lianjia.com/loupan/',
            'http://cs.fang.lianjia.com/loupan/',
            'http://qd.fang.lianjia.com/loupan/',
            'http://qh.fang.lianjia.com/loupan/',
            'http://dl.fang.lianjia.com/loupan/',
            'http://dg.fang.lianjia.com/loupan/',
            'http://sh.fang.lianjia.com/loupan/',
            'http://sz.fang.lianjia.com/loupan/',
            'http://su.fang.lianjia.com/loupan/',
            'http://sjz.fang.lianjia.com/loupan/',
            'http://san.fang.lianjia.com/loupan/',
            'http://fs.fang.lianjia.com/loupan/',
            'http://tj.fang.lianjia.com/loupan/',
            'http://gz.fang.lianjia.com/loupan/',
            'http://wh.fang.lianjia.com/loupan/',
            'http://wc.fang.lianjia.com/loupan/',
            'http://wn.fang.lianjia.com/loupan/',
            'http://hz.fang.lianjia.com/loupan/',
            'http://hk.fang.lianjia.com/loupan/',
            'http://hf.fang.lianjia.com/loupan/',
            'http://xm.fang.lianjia.com/loupan/',
            'http://xa.fang.lianjia.com/loupan/',
            'http://jn.fang.lianjia.com/loupan/',
            'http://yt.fang.lianjia.com/loupan/',
            'http://ls.fang.lianjia.com/loupan/',
            'http://zs.fang.lianjia.com/loupan/',
            'http://zh.fang.lianjia.com/loupan/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # self.logger.warning(str(response.url) + ' ' + str(response.status))
        page_data = response.xpath('/html/body//div[@class="list-wrap"]//div[@class="page-box house-lst-page-box"]/@page-data').extract()
        if page_data:
            page_data = JSONDecoder().decode(page_data[0])
        else:
            page_data = None
        house_list = response.xpath('/html/body//div[@class="list-wrap"]/ul[@class="house-lst"]/li')
        source = str(urlparse(response.url)[0]) + '://' + str(urlparse(response.url)[1])
        city = response.xpath('/html/body/div[@class="intro clear"]//a[last()]/text()').extract()
        if city:
        	city = str(city[0])[:-2]
        else:
        	city = ''
        self.logger.warning(str(response.url) + ' ' + str(response.status) + ' ' + str(page_data) + ' ' + str(len(house_list.extract())) + ' ' + str(city))
        for house in house_list:
            name = house.xpath('.//div[@class="info-panel"]/div[@class="col-1"]/h2/a/text()').extract()
            href = house.xpath('.//div[@class="info-panel"]/div[@class="col-1"]/h2/a/@href').extract()
            house_type = house.xpath('.//div[@class="info-panel"]/div[@class="col-1"]/div[@class="area"]/child::node()').extract()
            title_img = house.xpath('.//div[@class="pic-panel"]//img/@data-original').extract()
            price = house.xpath('.//div[@class="info-panel"]/div[@class="col-2"]//div[@class="average"]/span/text()').extract()
            address = house.xpath('.//div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span/text()').extract()
            tags = house.xpath('.//div[@class="info-panel"]/div[@class="col-1"]/div[@class="type"]/*/text()').extract()
            # print(name, href, house_type, title_img, price, address, tags)
            yield {
                'name': self.concat_list(name),
                'href': source + self.concat_list(href),
                'city': city,
                'house_type': self.concat_list(house_type),
                'title_img': self.concat_list(title_img),
                'price': self.concat_list(price),
                'address': self.concat_list(address),
                'source': source,
                'tags': tags
            }

            if page_data:
                pn = int(page_data['totalPage'])
                curr = int(page_data['curPage'])
                if curr < pn:
                    next_href = source + '/loupan/pg' + str(curr + 1)
                    yield scrapy.Request(url=next_href, callback=self.parse)

    def concat_list(self, lst):
        concated = ''
        for item in lst:
            concated += str(item) + ','
        return concated.rstrip(',')
