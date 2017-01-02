import scrapy
import logging
import regex
from urllib.parse import urlparse


class soufang_spider(scrapy.Spider):

    name = 'soufang'

    def start_requests(self):
        urls = [
            'http://newhouse.anshan.fang.com/house/s/',
            'http://newhouse.fang.com/house/s/',
            'http://newhouse.bd.fang.com/house/s/',
            'http://newhouse.bt.fang.com/house/s/',
            'http://newhouse.bengbu.fang.com/house/s/',
            'http://newhouse.bh.fang.com/house/s/',
            'http://newhouse.changchun.fang.com/house/s/',
            'http://newhouse.cd.fang.com/house/s/',
            'http://newhouse.cq.fang.com/house/s/',
            'http://newhouse.cs.fang.com/house/s/',
            'http://newhouse.cz.fang.com/house/s/',
            'http://newhouse.dl.fang.com/house/s/',
            'http://newhouse.dg.fang.com/house/s/',
            'http://newhouse.daqing.fang.com/house/s/',
            'http://newhouse.fs.fang.com/house/s/',
            'http://newhouse.fz.fang.com/house/s/',
            'http://newhouse.gz.fang.com/house/s/',
            'http://newhouse.ganzhou.fang.com/house/s/',
            'http://newhouse.gy.fang.com/house/s/',
            'http://newhouse.guilin.fang.com/house/s/',
            'http://newhouse.hz.fang.com/house/s/',
            'http://newhouse.hs.fang.com/house/s/',
            'http://newhouse.nm.fang.com/house/s/',
            'http://newhouse.hrb.fang.com/house/s/',
            'http://newhouse.hd.fang.com/house/s/',
            'http://newhouse.huaian.fang.com/house/s/',
            'http://newhouse.huzhou.fang.com/house/s/',
            'http://newhouse.hf.fang.com/house/s/',
            'http://newhouse.huizhou.fang.com/house/s/',
            'http://newhouse.hengyang.fang.com/house/s/',
            'http://newhouse.hn.fang.com/house/s/',
            'http://newhouse.jn.fang.com/house/s/',
            'http://newhouse.jining.fang.com/house/s/',
            'http://newhouse.jl.fang.com/house/s/',
            'http://newhouse.jy.fang.com/house/s/',
            'http://newhouse.jx.fang.com/house/s/',
            'http://newhouse.jm.fang.com/house/s/',
            'http://newhouse.jiujiang.fang.com/house/s/',
            'http://newhouse.jh.fang.com/house/s/',
            'http://newhouse.ks.fang.com/house/s/',
            'http://newhouse.km.fang.com/house/s/',
            'http://newhouse.lc.fang.com/house/s/',
            'http://newhouse.lf.fang.com/house/s/',
            'http://newhouse.linyi.fang.com/house/s/',
            'http://newhouse.ly.fang.com/house/s/',
            'http://newhouse.lyg.fang.com/house/s/',
            'http://newhouse.lz.fang.com/house/s/',
            'http://newhouse.liuzhou.fang.com/house/s/',
            'http://newhouse.leshan.fang.com/house/s/',
            'http://newhouse.mas.fang.com/house/s/',
            'http://newhouse.nanjing.fang.com/house/s/',
            'http://newhouse.nb.fang.com/house/s/',
            'http://newhouse.nt.fang.com/house/s/',
            'http://newhouse.nc.fang.com/house/s/',
            'http://newhouse.nn.fang.com/house/s/',
            'http://newhouse.qd.fang.com/house/s/',
            'http://newhouse.qhd.fang.com/house/s/',
            'http://newhouse.qz.fang.com/house/s/',
            'http://newhouse.sy.fang.com/house/s/',
            'http://newhouse.sjz.fang.com/house/s/',
            'http://newhouse.sh.fang.com/house/s/',
            'http://newhouse.sz.fang.com/house/s/',
            'http://newhouse.suzhou.fang.com/house/s/',
            'http://newhouse.sx.fang.com/house/s/',
            'http://newhouse.st.fang.com/house/s/',
            'http://newhouse.sanya.fang.com/house/s/',
            'http://newhouse.sq.fang.com/house/s/',
            'http://newhouse.tj.fang.com/house/s/',
            'http://newhouse.ts.fang.com/house/s/',
            'http://newhouse.taiyuan.fang.com/house/s/',
            'http://newhouse.taizhou.fang.com/house/s/',
            'http://newhouse.wuhan.fang.com/house/s/',
            'http://newhouse.wuxi.fang.com/house/s/',
            'http://newhouse.wf.fang.com/house/s/',
            'http://newhouse.weihai.fang.com/house/s/',
            'http://newhouse.wuhu.fang.com/house/s/',
            'http://newhouse.xj.fang.com/house/s/',
            'http://newhouse.wz.fang.com/house/s/',
            'http://newhouse.xian.fang.com/house/s/',
            'http://newhouse.xz.fang.com/house/s/',
            'http://newhouse.xm.fang.com/house/s/',
            'http://newhouse.xiangyang.fang.com/house/s/',
            'http://newhouse.xn.fang.com/house/s/',
            'http://newhouse.xt.fang.com/house/s/',
            'http://newhouse.yt.fang.com/house/s/',
            'http://newhouse.yz.fang.com/house/s/',
            'http://newhouse.yancheng.fang.com/house/s/',
            'http://newhouse.yc.fang.com/house/s/',
            'http://newhouse.yinchuan.fang.com/house/s/',
            'http://newhouse.yueyang.fang.com/house/s/',
            'http://newhouse.zz.fang.com/house/s/',
            'http://newhouse.zb.fang.com/house/s/',
            'http://newhouse.zhenjiang.fang.com/house/s/',
            'http://newhouse.zhoushan.fang.com/house/s/',
            'http://newhouse.zhangzhou.fang.com/house/s/',
            'http://newhouse.zh.fang.com/house/s/',
            'http://newhouse.zs.fang.com/house/s/',
            'http://newhouse.zhuzhou.fang.com/house/s/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # self.logger.warning(str(response.url) + ' ' + str(response.status))
        has_next = response.xpath('/html/body//div[@class="page"]/ul/li[@class="fr"]/a[@class="active"]/following::*[1]/@href').extract()
        house_list = response.xpath('/html/body//div[@class="nl_con clearfix"]/ul/li[not(@class)]')
        source = str(urlparse(response.url)[0]) + '://' + str(urlparse(response.url)[1])
        city = response.xpath('/html/body/div[@class="breadcrumb"]/div[@class="br_left"]/ul/li[1]/a/text()').extract()
        if city:
        	city = str(city[0])[:-2]
        else:
        	city = ''
        self.logger.warning(str(response.url) + ' ' + str(response.status) + ' ' + str(has_next) + ' ' + str(len(house_list.extract())))
        for house in house_list:
            name = house.xpath('.//div[@class="nlcd_name"]/a/text()').extract()
            href = house.xpath('.//div[@class="nlc_img"]/a/@href').extract()
            house_type = house.xpath('.//div[@class="house_type clearfix"]/child::node()').extract()
            title_img = house.xpath('.//div[@class="nlc_img"]/a/img/@src').extract()
            price = house.xpath('.//div[@class="nhouse_price"]/span/text()').extract()
            address = house.xpath('.//div[@class="address"]/a/@title').extract()
            tel = house.xpath('.//div[@class="tel"]/p/child::node()').extract()
            tags = house.xpath('.//div[@class="nlc_details"]//div[@class="fangyuan"]/*/text()').extract()
            # print(name, href, house_type, title_img, price, address, tel)
            yield {
                'name': self.concat_list(name),
                'href': self.concat_list(href),
                'city': city,
                'house_type': self.concat_list(house_type),
                'title_img': self.concat_list(title_img),
                'price': self.concat_list(price),
                'address': self.concat_list(address),
                'tel': self.concat_list(tel),
                'source': source,
                'tags': tags
            }
        if has_next:
            next_href = has_next[0]
            if not regex.search('\.', next_href):
                next_href = source + next_href
            yield scrapy.Request(url=next_href, callback=self.parse)

    def concat_list(self, lst):
        concated = ''
        for item in lst:
            concated += str(item) + ','
        return concated.rstrip(',')
