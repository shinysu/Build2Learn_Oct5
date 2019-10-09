"""
Content Extractor: extracts the title, first and last paragraph of a web page
"""

import bs4 as bs
import requests
import csv


def get_title(soup):
    """
    Extracts the title of the page
    :param soup: Beautiful Soup Object
    :return: String
    """
    return soup.title.string


def get_first_para(soup):
    """
    Extracts the first paragraph of the page
    :param soup: Beautiful Soup Object
    :return: String
    """
    return soup.find('p').getText()


def get_last_para(soup):
    """
    Extracts the last paragraph of the page
    :param soup: Beautiful Soup Object
    :return: String
    """
    return soup.find_all('p')[-1].getText()


def get_actions(html):
    """
    calls all other functions and sends back a list
    :param html: website html
    :return: list
    """
    soup = bs.BeautifulSoup(html, 'html.parser')
    return [get_title(soup), get_first_para(soup), get_last_para(soup)]


def write_csv_file(filename, write_data, m='a'):
    """
    writes or appends the data
    :param filename: name of the csv file
    :param write_data: can be a rows(list of lists) or just one list for rows
    :param m: a or write
    :return:
    """
    with open(filename, mode=m, encoding="utf8") as nav_file:
        writer = csv.writer(nav_file)
        writer.writerow(write_data)


if __name__ == '__main__':

    filename = "content_extractor.csv"
    urls = ['https://www.nemil.com/musings/four-startup-eng-killers.html']  # replace with get URLS function
    row = ["tite", "first para", "last para", "url"]
    write_csv_file(filename, row, "w")  # creating a new file for each run
    for url in urls:
        html = requests.get(url, timeout=10).content
        csv_row = get_actions(html)
        csv_row.append(url)
        write_csv_file(filename, csv_row)
