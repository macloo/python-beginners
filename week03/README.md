# Week 03: Python lists; reading and writing files

Students read chapters 4 and 8 in Sweigart. They also continue to learn about web scraping; that is covered in a separate part of this repo: [web_scraping](https://github.com/macloo/python-beginners/tree/master/web_scraping).

## Contents

* [Python lists](#python-lists)
  * [Augmented assignment operators](#augmented-assignment-operators)
  * [Methods, and finding things in lists](#methods-and-finding-things-in-lists)
  * [Tuples and immutability](#tuples-and-immutability)
  * [Lists and references](#lists-and-references)
  * [Review of key points from chapter 4](#review-of-key-points-from-chapter-4)
* [Reading and writing files with Python](#reading-and-writing-files-with-python)
  * [An alternative way to open a file](#an-alternative-way-to-open-a-file)
  * [Review of key points from chapter 8](#review-of-key-points-from-chapter-8)
* [Slides for Sweigart chapters 8 and 4](#slides-for-sweigart-chapters-8-and-4)

## Python lists

Python lists are very similar to JavaScript arrays. However, in Python, an **array** is a different thing, and we will be using lists, not arrays. [Read this if you're curious about the difference.](https://www.pythoncentral.io/the-difference-between-a-list-and-an-array/)

A new list can be made like this:

```python
my_list = ['cat', 'bat', 'rat', 'elephant']
```

As with JavaScript arrays, a Python list contains items that can be accessed via an index number. Each item in the list has a unique index, starting with 0:

```python
my_list = ['cat', 'bat', 'rat', 'elephant']
print(my_list[1])
# bat will be printed
```

This next bit is pretty sophisticated, but you will probably use it: We can put **lists *inside* of lists**. When we do, we can access the list items with index numbers as usual, but you'll need to use one index to access a list (in the list of lists) and a *second* index to access an item inside that list. See Sweigart page 81 for this. It's like a double-decker list.

**Slices** provide a way to get several consecutive items from a list all at once; see Sweigart pages 82-83. He calls it the multiple assignment trick.

The **length** of a list (just like the length of a string) can be found with `len()`:

```python
>>> my_list = ['cat', 'bat', 'rat', 'elephant']
>>> len(my_list)
4
>>> word = "fantastic"
>>> len(word)
9
>>>
```

Sweigart covers a variety of things we can do to or with Python lists, including adding new items to them and deleting items from them. Perhaps the most common thing we do with lists is **loop through them** to print or inspect their contents:

```python
>>> my_list = ['cat', 'bat', 'rat', 'elephant']
>>> for thing in my_list:
...   print(thing)
...
cat
bat
rat
elephant
>>>
```

If we need to know the index number while we are looping through a list, we can get it with `range()`:

```python
>>> my_list = ['cat', 'bat', 'rat', 'elephant']
>>> for i in range(len(my_list)):
...   print('The index: ' + str(i) + ' The item: ' + my_list[i])
...
The index: 0 The item: cat
The index: 1 The item: bat
The index: 2 The item: rat
The index: 3 The item: elephant
>>>
```

You don't need to loop through a list to find out if a particular item exists there. See Sweigart page 87 for details. He also shows you how to simply assign list items to variables (pages 87-88).

### Augmented assignment operators

I have no clue why this is in the middle of the lists chapter, but you should know that in Python we cannot increment a value with `++` as we can in JavaScript.

We can, however, use a shortened form instead of `x = x + 1` to increment a value:

```python
>>> x = 0
>>> x += 1
>>> print(x)
1
>>> x += 100
>>> print(x)
101
>>>
```

The same technique works with `-`, `*`, `\`, and `%` (modulus).

### Methods, and finding things in lists

In our web scraping exercises, we have been using a BeautifulSoup *method* that works on a string: `variable.get_text()`

A *method* is a function (e.g. `get_text()`), but it must be *called on* a *value*. In the `variable.get_text()` example, `variable` contains some text string that includes HTML tags we want to get rid of. Calling `get_text()` on `variable` returns the text without any HTML tags.

Sweigart shows us the *method* `index()`: If `spam` is a Python list and that list contains an item with the value `"hello"`, then `spam.index('hello')` will return the index number of that item.

It's useful to know that if the list *does not* contain that value, then the *method* `index()` will return a `ValueError`. This is useful because (like any error) `ValueError` could be used in a `try`/`except` combo. When you are scraping, that can be very useful indeed.

Other list methods include `append()` and `insert()`.

```python
>>> my_list = ['cat', 'bat', 'rat', 'elephant']
>>> my_list.append('rhino')
>>> print(my_list)
['cat', 'bat', 'rat', 'elephant', 'rhino']
```

The `append()` method is used often in web scraping.

Earlier in the chapter, we saw `del spam[2]` &mdash; this deletes the item with **index** 2 from the list `spam`. Note how different that is from the `remove()` method:

```python
>>> my_list = ['cat', 'bat', 'rat', 'elephant', 'rhino']
>>> my_list.remove('bat')
>>> print(my_list)
['cat', 'rat', 'elephant', 'rhino']
>>>
```

The `sort()` method will only work if your list items are all strings or all numbers. Also, strings that begin with an uppercase letter will be sorted separately from strings that begin with a lowercase letter.

```python
>>> water_list = ['lake', 'Ontario', 'river', 'Hudson', 'ocean', 'Atlantic']
>>> water_list.sort()
>>> print(water_list)
['Atlantic', 'Hudson', 'Ontario', 'lake', 'ocean', 'river']
>>>
```

Note that by using the `sort()` method, we changed the list. The old order cannot be regained. We destroyed all the old indexes. Originally, `water_list[0]` was `'lake'`. Now it is `'Atlantic'`.

There is a *method* Sweigart did not cover, and it's very handy: `pop()`. We can put an index inside the parentheses, and then the item at that index will be removed, permanently, from the list. If no index is specified, `pop()` removes *and returns* the *last* item in the list. Note that leaving the parentheses empty is *the most common way* to use `pop()`. Here's how it works:

```python
>>> print(water_list)
['Atlantic', 'Hudson', 'Ontario', 'lake', 'ocean', 'river']
>>> water_list.pop()
'river'
>>> next_item = water_list.pop()
>>> another_item = water_list.pop()
>>> print(water_list)
['Atlantic', 'Hudson', 'Ontario']
>>> print(next_item)
ocean
>>> print(another_item)
lake
>>>
```

[Here are all of the methods of Python lists.](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Tuples and immutability

Sweigart explains the difference between mutable and immutable data types and then goes on to introduce tuples (pronounced *too-puls*). A tuple might look like a list at first glance, but it's not &mdash; and it doesn't behave like a list, either.

A tuple can contain one or more items, like a list, but the items cannot be changed. They cannot be sorted into order, and they cannot be deleted or removed. Perhaps most surprising, you cannot even add a new item to a tuple. Once it is made, a tuple is *immutable*.

Lists are *mutable*, and that means we can change and reorder their contents at any time.

### Lists and references

Another important thing to know about Python lists is that you can't simply duplicate one. You might think, “Oh, I'm going to change the contents of `my_list`, so I'll make a copy of it as a backup.” This is not going to do what you probably expect:

```python
>>> my_list = ['cat', 'bat', 'rat']
>>> foobar = my_list
>>> print(foobar)
['cat', 'bat', 'rat']
>>> # you think you have a copy of my_list in foobar - you are wrong
>>> my_list.append('aardvark')
>>> my_list.append('zebra')
>>> my_list.remove('rat')
>>> my_list.sort()
>>> print(my_list)
['aardvark', 'bat', 'cat', 'zebra']
>>> print(foobar)
['aardvark', 'bat', 'cat', 'zebra']
>>>
```

Sweigart explains this at the end of his chapter 4. Both `my_list` and `foobar` are simply *references* to the list, which exists elsewhere in memory. To make a real copy that is independent of the original, you have to use other means.

### Review of key points from chapter 4

1. Create a new list
2. Get the value of one item in a list using its index
3. Make a double-decker list (lists inside a list) and access the items in the inner lists.
4. Use slices to get multiple items from a list all at once
5. Use `len()` to get the number of items in a list
6. Use `del()` to delete an item from a list
7. Loop through a list two different ways (one way uses `range()` and the other does not)
8. Increment a value using `+=`
9. Use the following *methods* correctly:
    * `index()`
    * `append()`
    * `remove()`
    * `sort()`
    * `pop()` *not in Sweigart; see above*
10. The differences between a Python list and a tuple
11. You can't simply make a copy of a list in the way you might expect (know how to look up the *correct way* to make a copy if you need to do so)

## Reading and writing files with Python

Python can access files on your computer. It can create new text files and write into them. It can also read text files and copy things from them.

In Sweigart’s chapter 8, we are mainly interested in pages 180–183. Nevertheless, his section under “Files and File Paths” contains useful information, and we will certainly use `import os` in some of our scraping work.

Most students will benefit from a review of “Absolute vs. Relative Paths” (page 175).

`os.path.isfile()` can be very useful if your program needs to check for the existence of a file in the current directory on your computer:

```python
filename = "my_data.txt"
# check if that filename is already in use
if ( os.path.isfile(filename) ):
    # ask user for a new filename if the other name exists
    filename = input("What should the filename be? ")
```

Sweigart explains the `readlines()` method (pages 182-183), but he does not cover the `readline()` method, which reads exactly *one* line at a time. These two different methods come in handy for solving different problems.

```python
>>> myfile = open('temp.txt', 'w')
>>> myfile.write('hello my little file\n')
21
>>> myfile.write('goodbye my little file\n')
23
>>> myfile.close()
>>> myfile = open('temp.txt')
>>> print( myfile.readline() )
hello my little file

>>> print( myfile.readline() )
goodbye my little file

>>> myfile.close()
>>>
```

Compare that with this:

```python
>>> myfile = open('temp.txt')
>>> print( myfile.readlines() )
['hello my little file\n', 'goodbye my little file\n']
>>> myfile.close()
>>>
```

Notice that the *newline character* (`\n`) is included above. You can **strip** that out with the string method `.strip()` &mdash; it removes spaces at both the start and the end of a string. If you want `.strip()` to remove other characters, put them inside the prentheses: `.strip(\t\n)` will remove both tabs (`\t`) and newlines (`\n`) but not spaces.

```python
>>> my_string = "   Hello, little    foobar  !!!     "
>>> print(my_string)
   Hello, little    foobar  !!!     
>>> print(len(my_string))
36
>>> my_string = my_string.strip()
>>> print(my_string)
Hello, little    foobar  !!!
>>> print(len(my_string))
28
>>>
```

Everything else in chapter 8 can be considered background information. Make a mental note about “pretty print,” though (page 185) &mdash; there will come a time when you'll be glad you remember it exists.

There's a method Sweigart does not cover, `seek()`. This comes in handy if you have a file open for reading and you have come to the bottom of it (perhaps by calling `readlines()`). Calling `seek(0)` on the File object returns to the *top* of the file so you can read or search its contents again.

```python
>>> myfile = open('temp.txt')
>>> file_lines = myfile.readlines()
>>> # next line: nothing happens
>>> print( myfile.readline() )

>>> myfile.seek(0)
0
>>> # next line: try it again
>>> print( myfile.readline() )
hello my little file

>>> myfile.close()
>>>
```

### An alternative way to open a file

This opens a File object (`f`) for appending, writes to it, closes it and saves it (without using `close()`). [Read more about it here.](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

```python
with open('myfile.txt', 'a') as f:
	words = "I would not like to eat any spam."
	f.write(words)
```

### Review of key points from chapter 8

1. “Call the `open()` function to return a File object” (Sweigart, page 181)
2. “Call the `read()` or `write()` method on the File object” (same)
3. “Close the file by calling the `close()` method on the File object” (same); this also *saves* the file
4. Distinguish between the File object and the contents of the file
5. Write filenames *without* path information when the file is in the same directory as your Python program
6. Call the `readlines()` method to create a **list** from a file with line breaks
7. The difference between the `readline()` method and the `readlines()` method
8. The difference between *write* mode (`'w'`) and *append* mode (`'a'`) with `open()`

## Slides for Sweigart chapters 8 and 4

[Slide deck](http://bit.ly/pythonrev3)
