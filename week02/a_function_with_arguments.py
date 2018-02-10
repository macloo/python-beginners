# Defines a function that takes 3 arguments.
# Arguments are passed in when you call the function.
# They are stored in variables specified in the first line of
# the function (these variables are called parameters).

# this function will do simple math to demonstrate the order of operations
# the parameters are a, b, c

def pemdas_demo(a, b, c):
    print("Demonstrate the expression " + str(a) + " + " + str(b) +
        " * " + str(c) + ":")
    result = a + b * c
    print(result)
    print("Demonstrate the expression (" + str(a) + " + " + str(b) +
        ") * " + str(c) + ":")
    result = (a + b) * c
    print(result)

# \n makes a newline
print("\nRun it once:")
pemdas_demo(3, 4, 5)

print("\nRun it a second time with different arguments:")
pemdas_demo(5, 4, 3)
