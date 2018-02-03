# Week 01

Students read chapters 1 and 2 in Sweigart. Some scripts in this folder are based on Sweigart’s &mdash; naturally, he has more examples than only these.

We start running simple expressions and statements in the interpreter:

```python
>>> fruit = 'apple'
>>> print(fruit)
apple
>>> fruit = 'pear'
>>> print(fruit)
pear
>>> 5 + 2
7
>>> sum = 5 + 2
>>> print(sum)
7
```

Until about halfway through chapter 1, Sweigart has us using the interactive Python interpreter, as seen above. Then he switches to writing a program in a file, which he assumes we will run in IDLE. However, we write our code in [Atom](https://atom.io/) and run it in Terminal (or PowerShell on Windows).

## Do not use IDLE to run your scripts

You can run any of the scripts in this folder in the manner described below.

In the middle of chapter 1 in [Automate the Boring Stuff with Python](http://automatetheboringstuff.com/), Sweigart invites you to leave the interactive Python shell (where you have the `>>>` prompt) and create a little program in a file.

Do not use IDLE. We are never using IDLE.

Instead, you can use Atom, our trusted code editor. Code is code. You can write any code in Atom. Instead of saving the file with a `.html` or `.js` extension, we save it with a `.py` extension when it is a Python file.

Then, how do you run it? Never try to run a file at the `>>>` prompt. You need to be at the bash prompt (`$`) in Terminal, or the PowerShell prompt if you’re using Windows.

It’s easiest if you are in the same directory where the `.py` file was saved. Use your `cd` command ([Command Line Tips](http://bit.ly/mm-commandline)) to get there.

At the bash prompt, type this (using your actual filename, of course)

```bash
python3 myfilename.py
```

And it runs!

Here’s where that comes in the chapter:

<img src="images/contents.png" alt="Book contents" width="50%">

Here’s what the program looks like in Atom:

<img src="images/atom.png" alt="Python code in Atom" width="75%">

Here’s how I ran it in Terminal (I made a folder named `automate` for my files from the book):

<img src="images/terminal.png" alt="Python 3 script running in Terminal" width="60%">

## Chapter review: chapters 1 and 2

These are the takeaways from the first two chapters.

### Chapter 1

1. Use the interactive Python shell to enter basic math expressions and get results (math operators)
2. Compare `23 / 7` and `23 // 7`
3. Exponents, e.g. `2 ** 4`
4. Order of operations: PEMDAS
5. Main data types: string, float, integer
6. String concatenation, e.g. `'Alice' + 'Bob'`
7. String replication, e.g. `'Alice' * 5`
8. Assign a value to a variable with `=`
9. Rules for variable names: No spaces. Can use only letters, numbers, and the underscore (\_) character. Cannot begin with a number. (p. 20)
10. Case sensitive
11. Comments start with `#`
12. `print()` function
13. `input()` function — assign it to a variable: `answer = input()`
14. `len()` function
15. `str()`, `int()`, and `float()` functions — when we insert a numeral into a string, for example (pp. 25–27)

### Chapter 2

1. The Boolean data type
2. Comparison operators, e.g. greater than, less than
3. Difference between `==` and `=` (what do they do?)
4. Boolean operators — `and`, `or`, `not`
5. Condition and block (p. 37ff) — blocks are indented
6. Flow control statements:
    - `if` statements — they will evaluate to `True` or `False`
    - `else` and `elif` statements
    - `while` loops
    - `break` statements (p. 49)
    - `continue` statements (p. 50)
    - `for` loops with `range()`
7. Press Control-C to break out of an infinite loop
8. What is an infinite loop?
9. “When used in conditions, `0`, `0.0`, and `''` (the empty string) are considered False, while all other values are considered True.” (Truthiness, p. 53)
10. The `random` module, from Python’s standard library
11. Use the `import` statement to import this module
12. Use `random.randint()`
