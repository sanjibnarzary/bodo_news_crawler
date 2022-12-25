# bodo_news_crawler
## Bodo News Crawler
Small scripts to crawl and extract Bodo Text from Bodosa News and Sentinel Bodo News

## Usage for Crawling Bodosa Newspaper
First make sure to add URLS and then execute
```
scrapy crawl bodonews
```
This will fetch and etract Bodo Text from the given URL. This is a very basic script it does not follow links.

## Usage for Crawling Sentinel Bodo
Make sure to give a particular Category URL
```
scrapy crawl sentinel
```
This is intermedia script it will follow links and extract the page contents from the url it followed. However it can not follow the categories.

Already crawled datas may contain extra data which needed cleaning.

## How to cite
Find it useful? Cite
```
@inproceedings{bodonewscrawler2022,
	title = {Web crawler for Bodo News Data from Sentinel and Bodosa News},
  	author = {Sanjib Narzary},
	booktitle = {Bodo News Crawler},
	url = {https://github.com/sanjibnarzary/bodo_news_crawler},
	year = {2022},
}
```