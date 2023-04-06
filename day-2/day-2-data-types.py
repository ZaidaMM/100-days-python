# DATA TYPES

# STRINGS
"Hello"

  # Subscript, disects a string (strat counting from zero because of binary (zero and one))
print("Hello"[0])
print("123" + "345")

# INTEGERS
print(123 + 345)

  # Thousands separated with "_", and python interprets it as comas
print(123_345_678)

# FLOAT
print(3.14159) 

# BOOLEAN
print(True)
print(False)

# TYPE CHECKING and TYPE CONVERSION
num_char = len(input("What's your name? "))
print(type(num_char))

print("Your name has " + str(num_char) + " characters.")

a = float(123)
print(a)


# DATA TYPES
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
digit1 = int(two_digit_number[0])
digit2 = int(two_digit_number[1])

total = digit1 + digit2
print(total)
