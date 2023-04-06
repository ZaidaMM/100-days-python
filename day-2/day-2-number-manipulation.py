print(8 / 3) # always givs a float, even if it is a clean division
print(int(8 / 3)) #chops everything after the decimal point >> floor
print(8 // 3) #chops everything after the decimal point >> floor.  Eithout converting into interger
print(round(8 / 3)) #rounds to the nearest integer
print(round(8 / 3, 2)) #adding number of decimal places

# Using variables
result = 4 / 2
result /= 2
print(result)

# Keeping track
score = 0

# user scores a point
score += 1

print(score)