import requests, os,re
from bs4 import BeautifulSoup

urls= []
urls.append()

r = requests.get(urls[0])
soup = BeautifulSoup(r.text, 'html.parser')
for i in soup.find_all("li", class_="page"):
    link = i.find('a', href=True)
    if link is None:
        continue
    link = "https://goodporn.to/" + link['href']
    urls.append(link)

name = ((soup.find('title')).string.split("-")[1])
name = re.sub('[^a-zA-Z0-9 \n\.]', '', name)
folder = os.path.join(r'C:\Users\sshuv\Music\New folder (2)', name)
try:
    os.mkdir(folder)
    print("folder created ", folder)
except:
    pass
os.chdir(folder)
k = 0
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = []
    all = soup.find_all("a", class_="item")
    for a in all:
        link = a.get("href")
        links.append(link)
    for link in links:
        print(link)
        fname = name + str(k) + '.jpg'
        with open(fname, "wb") as f:
            im = requests.get(link)
            f.write(im.content)
            print("Running", fname)
            k += 1
            print(k)
    print(k)
