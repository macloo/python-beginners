# this script will scrape all the URLs from the given page
# and write them into a file - note, it gets ALL URLs

from urllib.request import urlopen
from bs4 import BeautifulSoup

# get the contents of one page
html = urlopen("http://en.wikipedia.org/wiki/Harrison_Ford")
bsObj = BeautifulSoup(html, "html.parser")

# name the text file that will be created or overwritten
filename = 'myfile.txt'

def capture_urls(filename, bsObj):
    # create and open the file for writing
    myfile = open(filename, 'w')

    # get all <a> elements
    links_list = bsObj.findAll("a")
    # get contents of all href="" attributes - loop
    for link in links_list:
        if 'href' in link.attrs:
            # write one href into the text file - \n is newline
            myfile.write(link.attrs['href'] + "\n")

    # close and save the file
    myfile.close()

# call the function
capture_urls(filename, bsObj)
