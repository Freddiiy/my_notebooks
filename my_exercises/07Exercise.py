"""
Assignment 7
This assignment requires you to work with selenium, BeautifullSoup and possibly regular expressions
The next couple of weeks we are going to ask you: the students to create the assignment. The plan is for every group, to find a suitable website and create a a question to ask about the data on the site. These questions should be available to everyone thursday at 8:30 here: https://docs.google.com/spreadsheets/d/1UCOG-fTx9J5-kpFZ4zC9X8Cl8kiPbOoZpPWwUOopZxE/edit?usp=sharing
Then for the weekly assignment you can choose between the different exercises presented on the specific week.
Fallback plan
If this plan has some startup trouble, I have made a backup exercise below that you can choose if you cant find a suitable exercise on the google sheet.
"""
import bs4

"""
Part 1: Preparing data
    Use selenium to go to dba.dk with any search phrase
    Find all products added today
    Find only those from ‘København og omegn’
    create a .py file containing above function as a module that will return the browser page source.
"""

import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def dba_find_products(search: str):
    base_url = "https://www.dba.dk/"

    options = Options()
    options.headless = True

    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    browser.get(f"https://www.dba.dk/soeg/?soeg={search}")
    browser.implicitly_wait(3)

    search_field = browser.find_element(By.ID, "searchField")
    search_field.send_keys(search)
    search_field.submit()

    browser.implicitly_wait(3)

    page_source = browser.page_source
    print(browser.current_url)
    soup = bs4.BeautifulSoup(page_source, "html.parser")

    search_results = soup.find("table")
    print(search_results)




if __name__ == "__main__":
    dba_find_products("Computer")

