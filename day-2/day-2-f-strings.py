score = 0
height = 1.8
isWinning = True

# print("Your score is " + str(score)) #old way

# f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# total life = 90 years
total_months = 90 * 12
total_weeks = 90 * 52
total_days = 90 * 365

int_age = int(age)

months = int_age * 12
weeks = int_age * 52
days = int_age * 365

remaining_days = round(total_days - days)
remaining_weeks = round(total_weeks - weeks)
remaining_months = round(total_months - months)

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")