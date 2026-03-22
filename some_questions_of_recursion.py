# some of recursion function 

#reverse string 

def revers_string(s):
    if(len(s) == 0):
        return s
    return revers_string(s[1:]) + s[0]

print(revers_string("hallo"))
print(revers_string("keviv"))


print("-------------------------------------- vivek learning python  -----------------------------------------------------------")
print("-------------------------------------- vivek learning python  -----------------------------------------------------------")


# check palindrome using recusive function

def is_palindrom (v):

    if(len(v) <= 1):
        return True
    if( v[0] !=  v[-1]):
        return False
    
    return is_palindrom(v[1:-1])


print(is_palindrom("madam"))
print(is_palindrom("Taware "))
