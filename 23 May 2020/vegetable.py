myfile = open ("original1.txt")
content = myfile.read()
myfile.close()

with open("original1.txt") as myfile:
    content = myfile.read()

print(content)
