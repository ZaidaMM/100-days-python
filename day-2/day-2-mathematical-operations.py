# 3 + 5
# 7 - 4
# 3 * 2
# print(type(6 / 3)) # division always gives a type of float in python
# 3 ** 2 # raise a number to a power (3 to the power of 2)

# Order of operations PEMDAS:
  # Parentheses
  # Exponents
  # Multiplication  # Division (The one most to the left is prioritised)
  # Addition  # Substraction (The one most to the left is prioritised)

# BMI CALCULATOR\
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_height = float(height)
int_weight = int(weight)
bmi = int_weight / int_height ** 2
print(int(bmi))