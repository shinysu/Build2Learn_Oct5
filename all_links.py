import bs4 as bs
import requests
import csv
import urllib.parse

page_navigation_dict = {}


'''Open the url file to get the urls'''
with open('url_file.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for [url] in csv_reader:
        try:
            source = requests.get(url, timeout=5)
            soup = bs.BeautifulSoup(source.text, 'html.parser')
            menulist = []
            for u in soup.find_all('a', href=True):
                abs_url = urllib.parse.urljoin(url, u['href'])   #Get the absolute URL rather than a relative path
                title = u.text
                menulist.append((title, abs_url))
            menulist = list(dict.fromkeys(menulist))     #remove duplicates
            page_navigation_dict[url] = menulist
        except requests.ConnectionError as e:
            print("Connection Error. Make sure you are connected to Internet.\n")
            print(str(e))
        except requests.Timeout as e:
            print("Timeout Error")
            print(str(e))
        except requests.RequestException as e:
            print("General Error")
            print(str(e))
        except KeyboardInterrupt:
            print("Keyboard interrupt")


with open('navbar.csv', mode='w') as nav_file:
    fieldnames = ['webpage', 'title_url']
    writer = csv.DictWriter(nav_file, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in page_navigation_dict.items():
        writer.writerow({'webpage': key, 'title_url': value})
