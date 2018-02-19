# Week 03: Python lists; reading and writing files

Students read chapters 4 and 8 in Sweigart. They also continue to learn about web scraping; that is covered in a separate part of this repo.

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

Slices provide a way to get several consecutive items from a list all at once; see Sweigart pages 82-83.

The length of a list (just like the length of a string) can be found with `len()`:

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

## Augmented Assignment Operators

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

## Methods

More to comes
