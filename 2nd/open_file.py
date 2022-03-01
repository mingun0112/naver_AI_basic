from importlib.resources import contents


f= open("hi.txt","r")
contents=f.read()
print(contents)
f.close()