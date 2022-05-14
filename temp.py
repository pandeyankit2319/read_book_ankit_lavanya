import time
import re
from time import sleep, strftime
from random import randint
import pandas
import numpy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BookRead:
    """
    Contains any logic related to interacting with udemy website
    """
    with open("C:\\NotesMasters\\WS.csv", 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["BookNames", "AuthorNames", "Star_Ratings"])
    # Initialize webdriver object
    chromedriver_path = r"C:\Softwares\chromedriver_win32\chromedriver.exe"
    webdriver = webdriver.Chrome(executable_path=chromedriver_path)
    DOMAIN = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=1"
    webdriver.get(DOMAIN)
    for x in range(1, 101):
        xp_title = '//*[@class="bookTitle"]/span[@itemprop="name"]'
        titles = webdriver.find_elements(By.XPATH, value=xp_title)
        book_list = [value.text for value in titles]
        xp_author = '//*[@class="authorName"]/span[@itemprop="name"]'
        author = webdriver.find_elements(By.XPATH, value=xp_author)
        author_list = [value.text for value in author]
        xp_ratings = '//*[@class="minirating"]'
        #xp_ratings = '//*[@class="pagination"]/span[@class="previous_page disabled"]/em[@class="current"]/class[@class="next_page"]'
        ratings = webdriver.find_elements(By.XPATH, value=xp_ratings)
        ratings_list = [value.text for value in ratings]
        #star_List = webdriver.find_element_by_class_name('//*[@class="greyText smallText uitext"]/span/text()').extract ()
        star_ratings = []
        review_ratings = []
        for item in ratings_list:
               star_ratings.append(item.split(" — ")[0].replace(" avg rating",""))
               review_ratings.append(item.split(" — ")[1].replace(" ratings",""))
        data = {'BookNames': book_list, 'AuthorNames': author_list , 'Average_list' : star_ratings , 'Review Rating' : review_ratings }
        df = pandas.DataFrame(data=data)
        df.to_csv("C:\\NotesMasters\\WSelenium.csv", encoding='utf-8', index=False, mode ='a',header = False)
        xp_nextpage = webdriver.find_element_by_class_name("next_page").click()
        sleep(5)
        if x == 1:
            links=webdriver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click()


    

    