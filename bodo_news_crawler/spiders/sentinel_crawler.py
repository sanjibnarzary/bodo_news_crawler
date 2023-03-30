import scrapy
import os.path

class BodoNewsSpider(scrapy.Spider):
    name = "sentinel"
    page = 0

    # create new directory
    dir_name = "sentinel"

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    sent_urls = []
    def start_requests(self):
        urls = [
            #'https://bodo.sentinelassam.com/',
            #"गेलेनाय"
            'https://bodo.sentinelassam.com/%E0%A4%B9%E0%A4%B0%E0%A4%96%E0%A4%BE%E0%A4%AC-%E0%A4%B0%E0%A4%BE%E0%A4%A6%E0%A4%BE%E0%A4%AC/',

        ]
        #for url in urls:
            #self.page += 1
        #    yield scrapy.Request(url=url, callback=self.parse)
        url_base = 'https://bodo.sentinelassam.com/%E0%A4%B9%E0%A4%B0%E0%A4%96%E0%A4%BE%E0%A4%AC-%E0%A4%B0%E0%A4%BE%E0%A4%A6%E0%A4%BE%E0%A4%AC/'
        for i in range(1,43):
            if i == 1:
                url = url_base
            else:
                url = url_base + f'{i}/'
            yield scrapy.Request(url=url, callback=self.parse)

    #हरखाब-रादाब
    #https://bodo.sentinelassam.com/%E0%A4%B9%E0%A4%B0%E0%A4%96%E0%A4%BE%E0%A4%AC-%E0%A4%B0%E0%A4%BE%E0%A4%A6%E0%A4%BE%E0%A4%AC/
    #0 - 42
    #गाहाय-रादाब
    #https://bodo.sentinelassam.com/%E0%A4%97%E0%A4%BE%E0%A4%B9%E0%A4%BE%E0%A4%AF-%E0%A4%B0%E0%A4%BE%E0%A4%A6%E0%A4%BE%E0%A4%AC/
    # 0 - 129
    # गेलेनाय
    # https://bodo.sentinelassam.com/%E0%A4%97%E0%A5%87%E0%A4%B2%E0%A5%87%E0%A4%A8%E0%A4%BE%E0%A4%AF/
    # 0-10
    # रंजानाय
    # https://bodo.sentinelassam.com/%E0%A4%B0%E0%A4%82%E0%A4%9C%E0%A4%BE%E0%A4%A8%E0%A4%BE%E0%A4%AF
    # 0 - 4
    def parse(self, response):
        title = response.css('title::text').get()
        content = response.css('div.story').xpath('//p/text()').getall()
        if len(content) == 0:
            self.page = self.page
            print("No content found")
        else:
            self.page += 1
            content = response.css('div.story').xpath('//p//text()').getall()
            filename = f'sentinel-horkhab-radab-{self.page}.txt'
            save_path = 'sentinel'
            complete_name = os.path.join(save_path, filename) 
            with open(complete_name, 'w', encoding="utf-8") as f:
                r ="\n"
                f.write('TITLE: '+title)
                f.write("\n")
                f.write(r.join(content))
                f.write("\n")
            self.log(f'Saved file {filename}')
        #next_pagination = response.css('div.pagination a.next::attr(href)').get()
        #self.sent_urls.append(next_page)
        #if next_pagination is not None:
        #    next_pagination = response.urljoin(next_pagination)
        #    yield scrapy.Request(next_pagination, callback=self.parse)
        
        next_page = response.css('div.article-text a.stretched-link::attr(href)').getall()
        #self.sent_urls.append(next_page)
        if len(next_page) !=0:
            for u in next_page:
                page = response.urljoin(u)
                #print(page)
                yield scrapy.Request(page, callback=self.parse)
        #print('\n'.join(self.sent_urls))