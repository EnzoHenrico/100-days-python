# -- day 2 -- #

# ----- Type checking ----- #

# the type() function can return exactly the type of data you pass as parametter
type("I'm a string :)")

# ----- Type convetion ----- #

# To string
a = str(123)
print(type(a))

# To int
b = int("123")
print(type(b))

# To float
c = float("123.3")
print(type(c))

# ----- Type convetion Exercise ----- #

# Wrigt a code that sum a two digit input 

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))
