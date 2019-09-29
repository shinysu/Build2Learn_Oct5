import bs4 as bs
import requests
import csv
import operator

menu = {}


'''Open the url file to get the urls'''
with open('url_file.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for [url] in csv_reader:
        source = requests.get(url)
        soup = bs.BeautifulSoup(source.text,'html.parser')
        nav = soup.nav
        if nav:
            for u in nav.find_all('a'):
                if u.text in menu.keys():
                    menu[u.text] += 1
                else:
                    menu[u.text] = 1


sorted_menu = dict(sorted(menu.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_menu)


with open('navbar.csv', mode='w') as nav_file:
    fieldnames = ['page', 'count']
    writer = csv.DictWriter(nav_file, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in sorted_menu.items():
        writer.writerow({'page': key, 'count': value})
