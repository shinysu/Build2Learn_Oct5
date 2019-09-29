import bs4 as bs
import requests
import csv
import urllib.parse

page_navigation_dict = {}


'''Open the url file to get the urls'''
with open('url_file.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for [url] in csv_reader:
        source = requests.get(url)
        soup = bs.BeautifulSoup(source.text, 'html.parser')
        nav = soup.nav
        menulist = []
        if nav:
            for u in nav.find_all('a', href=True):
                abs_url = urllib.parse.urljoin(url, u['href'])   #Get the absolute URL rather than a relative path
                menulist.append(abs_url)
        menulist = list(dict.fromkeys(menulist))     #remove duplicates
        page_navigation_dict[url] = menulist


with open('navbar.csv', mode='w') as nav_file:
    fieldnames = ['webpage', 'nav_urls']
    writer = csv.DictWriter(nav_file, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in page_navigation_dict.items():
        writer.writerow({'webpage': key, 'nav_urls': value})
