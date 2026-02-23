# slicing using index number

str = "vivek_taware 🙏 "
print(str[0:3])
print(str[1:6])
print(str[13])
print(str[:12])
print(str[5:])

#ends with function

str = "apna college india from pune india"
str = str.capitalize()
print(str.endswith("ia"))
print(str.capitalize())

# replace
print(str.replace("o","V"))
print(str.replace("pune","akluj"))


# find function returns first index number of that word 
print(str.find("p"))
print(str.find("o"))
print(str.find("b"))# that latter doesn't exist in our string