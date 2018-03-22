myfile = open('jabberwocky.txt')
content = myfile.read()
# now content holds the contents of jabberwocky.txt
myfile.close()

newfile = open('anewfile.txt', 'w')
newfile.write(content)
# now content has been written into a new file 
newfile.close()
