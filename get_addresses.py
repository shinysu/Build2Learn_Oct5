"""
1. Get the contact us page from the website
2. Get the address from the website
"""

import requests
from bs4 import BeautifulSoup
import re
import json
import ast


def get_contact_page(html):
    """
    gives back the contact us link
    :param html: page html
    :return: one link - contact us - string
    """
    soup = BeautifulSoup(html, "html.parser")
    for a_tag in soup.find_all('a', href=True):
        # print(a_tag.text)
        if "contact" in a_tag.text.lower():
            return a_tag["href"]
    return None


def get_cities(filename="cities-name-list.json"):
    """
    get all city names from India
    :param filename: file name for the json
    :return: tuple of cities
    """
    with open(filename, "r") as json_file:
        content = json_file.read()
        lst = ast.literal_eval(content)
        return tuple(lst)


def has_city(text):
    """
    Checks if a city is there in a given Paragraph
    :param text: string
    :return: Boolean
    """
    cities = get_cities()
    for word in text.split():
        if word in cities:
            return True
    return False


def get_address(html):
    """
    returns the address for a given contact us page
    :param html:
    :return: string
    """
    addresses = []
    soup = BeautifulSoup(html, "html.parser")
    p = soup.findAll("p")
    for paras in p:
        if has_city(paras.text):
            addresses.append(paras.text)
    return addresses


if __name__ == '__main__':
    url = "https://hindustanschools.in"
    contact_page = get_contact_page(requests.get(url).content)
    print(contact_page)
    if contact_page:
        if contact_page.startswith("/") or not contact_page:
            contact_page = url + contact_page
        html = requests.get(contact_page).content
        print(get_address(html))

"""
TODO: Add a smarter way to get the address parent element. Sometimes the parent element can be divs -
Use BeautifulSoup to go one step up if \n is less than 3
"""
