# some of recursion function 

#reverse string 

def revers_string(s):
    if(len(s) == 0):
        return s
    return revers_string(s[1:]) + s[0]

print(revers_string("hallo"))