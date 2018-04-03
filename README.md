# Python Beginners

Used in conjunction with the book [Automate the Boring Stuff with Python](http://automatetheboringstuff.com/), by Al Sweigart (2015). There is a link to download his code under "Additional Content" on that page.

Since 2012, I have been teaching Python to journalism students. I used to use a set of tutorials called *Learn Python the Hard Way*. I sought a new set of instructions suitable for my students, whose previous experience with programming is recent and limited to client-side JavaScript.

I adopted Sweigart’s text in 2017 after examining several others. I’m really pleased with the way he introduces the basics of Python 3. I decided to abandon Python 2 in 2017, and it’s great to have found a beginner text that explains enough but not too much. I love Sweigart’s style and his examples.

The one thing I dislike in Sweigart’s book is his assumption that we would be using IDLE. We write our code in [Atom](https://atom.io/) and run it in Terminal (or PowerShell on Windows).

## One-time how-to documents

* [Command Line Tips](http://bit.ly/mm-commandline) &mdash; How to navigate among your files and folders in the Terminal.
* [Getting Started with Python 3](http://bit.ly/py3-quick-install) &mdash; How to install Python 3 and get it running.
* [Creating or using requirements.txt](http://bit.ly/python-reqs) &mdash; How to install the libraries and extensions know as *dependencies* for a Python project or app. It is not necessary to read this until week 5 or later.

## About this repo

Below you'll see an overview of the contents. Within each folder, you'll find a README and example Python files. In the course, we cover web scraping with Python and also web apps using the Flask framework. Inside the [web_scraping](web_scraping) folder and the [flask](flask) folder here, you'll find a lot more information and examples.

In the course, we spend about four weeks on scraping and another four weeks on Flask.

## Week 01

Students read chapters 1 and 2 in Sweigart. Some scripts in the **week01** folder are based on Sweigart’s &mdash; naturally, he has more examples than only these. See the README in the [week01](week01) folder for more information.

Example files in this folder cover if-statements, for-loops, while-loops, and `random.randint`. Also (very basic): `print()`, `input()`, `len()`.

## Week 02

Students read chapter 3, “Functions,” in Sweigart. See the README in the [week02](week02) folder for more information.

Example files in this folder cover functions, arguments, the `return` statement, scope of variables, and exception handling: `try`/`except`.

Writing modular code is not only a good practice; it also helps you to write functions you can test reliably and reuse in future work. See [modular-code](week02/modular-code) in the **week02** folder for more information.

## Week 03

Students read chapters 4 and 8 in Sweigart. See the README in the [week03](week03) folder for more information.

Example files in this folder cover loops and lists, and how to open, read, and close files.

Chapter 4 covers just about everything one needs to know about **Python lists**. The README highlights some of the methods, etc., we will use most often, including some things Sweigart does not cover.

Chapter 8 covers **reading and writing files** with Python. The information we need most often is on pages 180-183. There are a couple of things not covered that I have explained in the README.

## Week 04

Students read Chapters 5 in Sweigart and learn about **Python dictionaries**. See the README in the [week04](week04) folder for more information.

## Jupyter Cheat Sheet

Students use Jupyter Notebook to complete several assignments. The [cheat sheet](jupyter_cheat_sheet) is helpful after Jupyter Notebook has been installed and they need to launch it, save their work, and close it correctly.

## Web scraping

Students are introduced to web scraping with the BeautifulSoup library in the second week. See the README in the [web_scraping](web_scraping) folder for instructions to install BeautifulSoup, as well as some basic uses of this scraping library.

### Mitchell, chapter 3

The README in the [mitchell-ch3](web_scraping/mitchell-ch3) folder supplements chapter 3 in *Web Scraping with Python*, by Ryan Mitchell. The chapter is very challenging for beginners, so here are a couple of `.py` files and examples to ease the way.

Example files are included for scraping all URLs from a page, and for scraping the same data items from numerous pages, using a list of URLs.

### Mitchell, the rest of the book

The README in the [more-from-mitchell](web_scraping/more-from-mitchell) folder highlights the points we cover in our third week with *Web Scraping with Python*, by Ryan Mitchell. We don’t have time to read the entire book, so we need to jump around and get acquainted with some common scraping problems and their solutions.

This section includes using Selenium, HTTP headers, writing scraped data to CSV files, the sleep timer in Python, and parsers.

Example files are included for writing scraped data to CSV files and to a MySQL database, using Selenium, and sending email from a Python script.

## Flask

Students are introduced to Flask, a Python framework, in the fifth week of Python. See the README in the [flask](flask) folder for details.

This section has several parts, explaining templates, app deployment, **Flask-WTF** forms, and **Flask-SQLAlchemy** for database apps.
