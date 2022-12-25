import scrapy
import os.path

class BodoNewsSpider(scrapy.Spider):
    name = "bodonews"
    page = 0
    def start_requests(self):
        urls = [
            ''
        ]
        for url in urls:
            #self.page += 1
            yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response):
        self.page += 1
        title = response.css('title::text').get()
        content = response.css('section.tcb-post-content').xpath('//p/text()').getall()
        print(title,content)
        filename = f'bodosa-{self.page}.txt'
        save_path = 'out'
        completeName = os.path.join(save_path, filename) 
        with open(filename, 'w', encoding="utf-8") as f:
            r ="\n"
            f.write(title)
            f.write("\n")
            f.write(r.join(content))
            f.write("\n")
        self.log(f'Saved file {filename}')