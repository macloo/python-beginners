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

Near the end of chapter 3, Sweigart gives us a program that (oddly enough) does not include any functions. Let’s *refactor* his program to make it more modular, using functions.

**Problem to be solved:** Create a game in which a user gets six tries to guess a random number.

**Pseudo code:**

1. Get a random number.
2. Ask player to guess it.
3. Check if guess was right.
4. Repeat until either the guess is right or the player runs out of tries.
5. Tell the player the result.

**How to start:**

```python
# get random number
# take guesses from user and check each guess
# tell user the result
```

**Build the main function:**

If you build your main function around your pseudo code, you should be able to make it very modular. *Modular* can mean each function accomplishes one task. It’s not sensible to write a function that contains only one line, so don’t take this too literally.

Let’s begin by including in the main function only what seems absolutely necessary. Leave out anything that might get complicated.

```python
import random

def guess_number():
    # get random number
    secret_number = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20.")
    # take guesses from user and check each guess

    # tell user if they won or not

    # this function must tell us the outcome, so: message
    return message
```

“Take guesses from user and check each guess” is two tasks, but you will want to *loop* to ask the user to guess, capture the guess, and then check the guess against the correct answer. You can’t sensibly spit that into two separate functions.

Let’s *name* the two secondary functions and what they return before we write them:

```python
import random

def guess_number():
    # get random number
    secret_number = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20.")

    # take guesses from user and check each guess
    guesses = take_guesses(secret_number)

    # tell user if they won or not
    message = tell_result(guesses)

    return message
```

Now we know what we have to get out of the `take_guesses()` function: The number of guesses taken. If all guesses were used without a correct answer, we know the player failed.

**Think about this:** Knowing what you want to *return* helps you write a better function. Don’t just print things and throw them away. If you *return* something, you can store it in a variable.

Get started like this:

```python
# compare user input to the secret number
def take_guesses(secret_number):
    # give them 6 guesses
    for i in range(1, 7):
        # ask user for a guess, a number
        # if it's too high, tell them
        # if it's too low, tell them
        # if it's correct, return which guess this is
    return None
```

If they use all six guesses, the loop ends, and you know they never guessed the correct number. You return the `None` value. If they guessed correctly, you return a number: how many tries it took.  Below is the completed guessing function.

```python
# compare user input to the secret number
def take_guesses(num):
    # give them 6 guesses
    for i in range(1, 7):
        print("Take a guess.")
        # user enters a number - change string input to integer 
        guess = int( input() )
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            # if guess is correct, return number of guesses they took
            return i
    # if they are wrong all times and loop ended -
    return None
```


*more to come*
