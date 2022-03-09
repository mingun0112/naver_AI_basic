input="cat32dog16cow5"

def find_string(input):
    p=[]
    for i in input:
        i=ord(i)
        if i>=49 and i<=57:
            i=58
        i=chr(i)
        p.append(i)
    p = ''.join(p).replace("::", " ").replace(":"," ").split()
    return(p)

print(find_string(input))
