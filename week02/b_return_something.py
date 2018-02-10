# Defines a function that returns a sentence.

def fave_food():
    print("What is your favorite food?")
    food = input()
    if food == "pizza":
        response = "Mmm, Italian!"
    elif food == "veggies":
        response = "So healthy!"
    else:
        response = "Meh, not one of my favorites."
    return(response)

# the function definition has ended
# the following line stores whatever is returned by the
# function in the variable, opinion
opinion = fave_food()

# \n makes a newline
print("The function has run.\n... Nothing has been printed ...\n")

print(opinion)
