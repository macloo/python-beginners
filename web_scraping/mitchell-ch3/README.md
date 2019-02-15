# Mitchell chapter 3: More web scraping

You don’t need to thoroughly understand “Six Degrees of Kevin Bacon” to comprehend what Mitchell is doing in chapter 3, but it’s essential to understand what kind of URLs she wants to scrape from a selected Wikipedia page. In this case, she is getting all links from ONE Wikipedia page &mdash; [this one](https://en.wikipedia.org/wiki/Kevin_Bacon).

She wants only links to Wikipedia *article* pages. There will be many, many other links on an actor page at Wikipedia. How can she write her Python script to eliminate most or all of the links she doesn’t want?

These techniques are useful for scraping URLs from *any* web page &mdash; not just Wikipedia.

Notice how she begins to narrow the options. *Where* on the page are the desired URLs? And what makes the URLs she wants *different* from the ones she doesn’t want?

Remember to refer to Mitchell’s updated code, [here](https://github.com/REMitchell/python-scraping/blob/master/Chapter03-web-crawlers.ipynb). You can do a Command-f (Ctrl-f on Windows) to find any line of code on the page.

## Regular expressions to narrow the search

Regular expressions, also called regex, are hard. They just are. But they can be super useful. Mitchell first discussed regex in chapter 2, but we skipped over that. Sweigart does a much better job in his chapter 7, which you haven’t read yet.

We can use [this slide deck](http://bit.ly/mm-scrapeCh3-slides) to go through Mitchell's one regex statement for her Kevin Bacon scrape *in detail*.

```python
'^(/wiki/)((?!:).)*$'
```

That's her regex string, and essentially it says: 'Give me the URL only if it *begins with* `/wiki/`, and in the text following that, there is not even one colon.' (She explains about the colon in chapter 3.)

* Begins with `/wiki/`: `^(/wiki/)`
* All the text to the end of the string we're looking at: `(.)*$`
* With no colons in that text: `(?!:)`

Mitchell is looping through a Python **list** of `href` attributes.

Each item in the list is the contents of one `href` found on the first page she scraped (the Kevin Bacon page).

The regex string *evaluates* the item (the relative path, really, although we’ve been saying the URL) for the criteria listed above. **Print it** if it meets the criteria. **Ignore it** if it doesn’t.

Eventually we can get a list of about 400 relative paths, like this:

```bash
/wiki/Kevin_Bacon_(disambiguation)
/wiki/Philadelphia
/wiki/Pennsylvania
/wiki/Kyra_Sedgwick
/wiki/Sosie_Bacon
/wiki/Edmund_Bacon_(architect)
/wiki/Michael_Bacon_(musician)
/wiki/Footloose_(1984_film)
/wiki/JFK_(film)
/wiki/A_Few_Good_Men
/wiki/Apollo_13_(film)
/wiki/Mystic_River_(film)
/wiki/Sleepers
/wiki/The_Woodsman_(2004_film)
```

Add `https://en.wikipedia.org` to the left side of those, and we can write a script that opens page after page after page &mdash; or, in Mitchell’s example, we can choose a URL randomly from the big list and open that new page.

```python
'https://en.wikipedia.org' + articleUrl
```

## Scrape and repeat

Next, Mitchell starts to expand the script to make it do more. She doesn’t want only links from the Kevin Bacon page &mdash; she wants to collect links from other Wikipedia articles, reusing the same code. (She wrote: “You need to be able to take this code and transform it into something more like the following” ...)

Instead of opening every link from her Kevin Bacon list, Mitchell writes her script to select a random link. Here's where Python lists come in:

* Her function `getLinks()` takes one argument (`articleUrl`) and returns a **list** of relative paths that meet her criteria.
* She calls that function *the first time* with `links = getLinks('/wiki/Kevin_Bacon')` &mdash; meaning the list named `links` contains all the links from the Kevin Bacon Wikipedia page (returned by the function `getLinks()`).
* Her while-loop selects a random link from the list named `links`: `newArticle = links[random.randint(0, len(links)-1)].attrs['href']`
* If that seems impossible to figure out, look at it this way: `newArticle = links[0].attrs['href']` &mdash; that would get the `href` value from the *first item* in the list named `links`. Because the index 0 means the first item.
* Instead of 0, `random.randint(0, len(links)-1)` is going to get a random number from 0 to the length of the list, minus 1, because the last item in a 400-item list is `listname[399]`.
* Her while-loop then **replaces** the contents of the list named `links` with the links from the new page: `links = getLinks(newArticle)`

Note that her while-loop is likely to be an infinite loop!

## Scrape and repeat without randomness

You might never need to crawl an entire website, but it is very likely you *will want to* crawl multiple pages on a website.

Mitchell discusses how we can use Python's `set()` function to avoid collecting duplicate URLs. This will not be a problem for every scraping project, but it’s nice to know that `set()` can help us prevent duplicate URLs in our list, if it seems likely that duplicates could sneak in.

Under the heading “Collecting Data Across an Entire Site,” Mitchell starts to discuss what we usually, or almost always, want to do when scraping: Not just get URLs, but get some specific information from *each page* represented by those URLs.

Note that Mitchell’s code is still simply *printing* what we find. She’s not yet saving the information into a file or files.

Below is a simplified version of Mitchell’s code from this section: It merely prints some information from each page in a list named `link_list`.

```python
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
    html = urlopen('https://en.wikipedia.org' + pageUrl)
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
        print('------------')
    except AttributeError:
        print('This page is missing something! No worries though!')

# call the function
for link in link_list:
    getInfo(link)
```

You can find this code in *scrape_a_few_pages.py* in this repo. Run it and see what you get.

## Next steps

The file *scrape_all_urls.py* in this repo demonstrates how to scrape all the links from one Wikipedia page (note: ALL of the links, not just links for the article pages) and write them into a text file. You should run this file and make sure you understand how it works. You can change the URL in `html = urlopen()` to scrape URLs from *any* Wikipedia page. Try it!

As we move forward, you’ll find that **many or most scraping projects have two stages:** First, we collect the URLs of all the pages from which we need to scrape data. Second, we loop through the URLs: (1) creating a BeautifulSoup object for a page; (2) extracting the data we desire; and then (3) moving on to the next page, and so on &mdash; for as many pages as we need to scrape.

This means we will usually be writing one Python script to scrape the URLs, and another, separate Python script to scrape data from each page.

Or we might write two separate *functions,* but have both of them in one `.py` file.

Mitchell’s section under the heading “Crawling Across the Internet” contains useful ideas, but don’t worry too much about her code there &mdash; you will not be making Google!
