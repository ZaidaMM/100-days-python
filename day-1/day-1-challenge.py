# 1. Create a greeting for your program
greeting = ("Hi " + input("What's your name: ") + "!")
print(greeting)
# 2. Ask the user for the city they grew up in
city = input("Which city did you grow up in? \n")
# 3. Ask the user for the name of a pet
pet = input("What's the name of your pet? \n")
# 4. Combine the name of their city and pet and show them their band name
band_name = city.capitalize() + " " + pet.capitalize()
print("Your band name is %s" % (band_name))
# 5. Make sure the cursor shows in a new line
