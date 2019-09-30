'''Content Extractor: extracts the title, first and last paragraph of a web page'''

import bs4 as bs
import requests
import csv


def get_title(soup):
    '''Extracts the title of the page and writes it to the output csv file'''
    title = soup.title.string
    mode = 'w'
    write_csv_file([title], ["Title:"],mode)


def get_first_para(soup):
    '''Extracts the first paragraph of the page and appends it to the output csv file'''
    first_para = soup.find('p').getText()
    mode = 'a'
    write_csv_file([first_para], ["First Para:"], mode)


def get_last_para(soup):
    '''Extracts the last paragraph of the page and appends it to the output csv file'''
    last_para = soup.find_all('p')[-1].getText()
    mode = 'a'
    write_csv_file([last_para], ["Last para:"], mode)


def write_csv_file(write_data,text,m):
    '''writes or appends the csv file based on the mode, "m"'''
    with open('content_extractor.csv', mode=m) as nav_file:
        writer = csv.writer(nav_file)
        writer.writerow(text)
        writer.writerow(write_data)


url = 'https://www.nemil.com/musings/four-startup-eng-killers.html'
source = requests.get(url, timeout=10)
soup = bs.BeautifulSoup(source.text, 'html.parser')
get_title(soup)
get_first_para(soup)
get_last_para(soup)
