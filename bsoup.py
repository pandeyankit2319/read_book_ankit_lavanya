from bs4 import BeautifulSoup
import requests
from lxml import etree
import time
import pandas as pd
from lxml import html

# setting boolean parameter for page limit
page_limit = True

if page_limit == True:
    max_pages = 2
else: max_pages = 200


# declaring lists to store scraped data
bookName_list = []
author_list = []
rating_list = []
review_list=[]




# iterating over first 100 pages to scrap required data
for i in range(1, max_pages+1):
    url = 'https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page='+str(i)
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text
    tree = html.fromstring(html_content)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    dom = etree.HTML(str(soup))
    
    bookName = dom.xpath('//a[@class="bookTitle"]/span')
    for bookNme in range(len(bookName)):
        bookName_list.append(bookName[bookNme].text) 
    
    author_Name= dom.xpath('//*[@class="authorName"]/span')
    for authorNm in range(len(author_Name)):
        author_list.append(author_Name[authorNm].text)   
        
    rating_lists =tree.xpath('//*[@class="greyText smallText uitext"]/span/text()')
    for rating in rating_lists:
        rating_list.append(rating.split(" — ")[0].replace(" avg rating",""))
        
    review_lists=tree.xpath('//*[@class="greyText smallText uitext"]/span/text()')
    for rev in review_lists:
        review_list.append(rev.split(" — ")[1].replace(" ratings",""))
        
   
   
# creating a dictionary to store the scraped data in previous step
data_dictionary = {'Book': bookName_list, 'Author': author_list, 'Star_Ratings': rating_list, 'Review_Ratings' : review_list}


# storing the scraped data in csv file
#dataframe = pd.DataFrame(data_dictionary)
#dataframe.to_csv('data.csv', mode='a', index=False, header=False, encoding="cp1252")
df = pd.DataFrame.from_dict(data_dictionary, orient='index')
df = df.transpose()
df = df.sort_values(by=['Book'], ascending=True)
df.to_csv('data_bsoup.csv',index = False, encoding='utf-8')