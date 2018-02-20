from urllib.request import urlopen
from bs4 import BeautifulSoup

link_list = ['/wiki/A_Few_Good_Men',
    '/wiki/Apollo_13_(film)',
    '/wiki/Mystic_River_(film)',
    '/wiki/Fox_Broadcasting_Company',
    '/wiki/The_Following',
    '/wiki/Golden_Globe_Award',
    '/wiki/Screen_Actors_Guild_Awards',
    '/wiki/Primetime_Emmy_Award',
    '/wiki/The_Guardian']

def getInfo(pageUrl):
    html = urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id ="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
        print("------------")
    except AttributeError:
        print("This page is missing something! No worries though!")

for link in link_list:
    getInfo(link)
