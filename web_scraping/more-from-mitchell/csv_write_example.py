# create a new CSV file from a table on a web page
import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://weimergeeks.com/examples/scraping/example1.html")
bsObj = BeautifulSoup(html, "html.parser")

# open new file for writing -
csvfile = open("example.csv", 'w', newline='', encoding='utf-8')
# make a new variable, c, for Python's CSV writer object -
c = csv.writer(csvfile)

# there is only one table on this page - get it
table = bsObj.find("table")
# get all rows from table
tr_list = table.findAll("tr")
# loop over all the rows
for row in tr_list:
    # a temporary list that will be overwritten each time the loop runs
    tmp_row = []
    # get all cells from row
    td_list = row.findAll("td")
    # loop over all the td's in the current row - a loop inside a loop 
    for cell in td_list:
        # add one td (cell) to the list
        tmp_row.append( cell.get_text() )
    # when all td's are in the tmp_row list - write one row to csv
    c.writerow(tmp_row)

# close the file
csvfile.close()
