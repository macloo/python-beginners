# this file demos two ways to loop over a list
# same list, two ways

fruit_list = ['mango','apple','pear','banana','pomegranate']

print("\nFirst loop:\n")

for fruit in fruit_list:
    print(fruit)

print("\nSecond loop:\n")

for i in range( len(fruit_list) ):
    print( str(i + 1) + ". " + fruit_list[i] )

print("\nMore stuff:\n")

# remove last item from list, store it in a variable
item = fruit_list.pop()
print(item + " was removed ...")

print("Now there are " + str( len(fruit_list) ) + " items in the list.")
