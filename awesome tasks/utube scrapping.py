from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4
import ssl
import requests
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
# print(soup)

# match = soup.find('span', class_='style-scope yt-formatted-string')
# print(match)


# data = soup.find_all(class_='style-scope yt-formatted-string')
# data = soup.find("div", {"class" : "style-scope yt-formatted-string"})
# print(data)

res = requests.get('https://youtube.com/channel/UC9J_WMeNyoC0nlMSXFeoMFw/about')
soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup)