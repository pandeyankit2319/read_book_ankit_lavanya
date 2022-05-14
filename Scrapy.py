import scrapy
import csv
import pandas
from scrapy.crawler import CrawlerProcess

with open("C:\\NotesMasters\\WS.csv", 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["BookNames", "AuthorNames", "Star_Ratings","Review_Ratings"])

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = []
    for x in range (1,101):
        start_urls.append("https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=" + str(x))
    print(start_urls)
    def parse(self, response):
         bookNames_List = response.xpath('//a[@class="bookTitle"]/span/text()').extract ()
         author_List = response.xpath('//*[@class="authorName"]/span/text()').extract ()
         star_List = response.xpath('//*[@class="greyText smallText uitext"]/span/text()').extract ()
         star_ratings = []
         review_ratings = []
         for item in star_List:
            star_ratings.append(item.split(" — ")[0].replace(" avg rating",""))
            review_ratings.append(item.split(" — ")[1].replace(" ratings",""))
            data = {'BookNames': bookNames_List, 'AuthorNames': author_List , 'Star_Ratings' : star_ratings , 'Review_Ratings' : review_ratings}
         df = pandas.DataFrame(data=data)
         df.to_csv("C:\\NotesMasters\\Sel.csv", encoding='utf-8', index=False, mode ='a',header = False)
# run spider
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()