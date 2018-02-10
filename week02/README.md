# Week 02: Python functions

Students read chapter 3 in Sweigart. They also begin to learn about web scraping; that is covered in a separate part of this repo.

Now we start writing functions in Python3. We’ll write files in [Atom](https://atom.io/) and save them with the `.py` extension.

To run a function named `foobar.py` that’s in the current directory, type this at the bash prompt (`$`):

```bash
python3 foobar.py
```

Students can now write and save their Python3 code in files.

## Using parameters and returns in functions

Sweigart notes that many functions operate as “black boxes”: This describes a function with parameters (it takes arguments) and a `return` statement. Something goes into it (arguments) and something comes out of it (whatever is returned). You don’t need to know how it works; you just need to know what it does.

This is true for many functions we use from imported libraries, such as BeautifulSoup (for web scraping). We run a function such as this:

```python
print( varname.get_text() )
```

... and it prints only the text content from inside an HTML element (such as `title` or `li`) that is stored in `varname`. The variable `varname` contains the HTML tags (possibly quite a lot of tags), but the BeautifulSoup function `get_text()` removes them neatly, giving us just text. How does `get_text()` do that? *We don’t need to know.* That’s the beauty of a function as a black box: It just works.

We don’t need to know how a toaster toasts bread to get toast out of it. We put in two pieces of bread (the *arguments* we pass into a function), and toast is *returned* after the function runs.

## Building functions for every task in a program

Near the end of chapter 3, Sweigart gives us a program that (oddly enough) does not include any functions. In the folder named *modular-code*, we will walk through how to convert that program into a collection of three modular functions.

*Modular* can mean that each function accomplishes *one* task. It’s not sensible to write a function that contains only one line, so don’t take this too literally. However, writing a lot of small, short functions gives you an easy way to test and perfect each part of your program in a very manageable way.

It keeps the larger job &mdash; the complete program &mdash; from overwhelming you.
