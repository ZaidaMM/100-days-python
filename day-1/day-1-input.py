# The input("A prompt for the user") function, when it executes the program pauses waiting for the user's input, once given the input the program ends. Then we can use that data inside our code

# print("What is your name?") # this will only print the question, no prompt
# input("What is your name?")

# This will prompt the user, then will print the full sentence including the user's input
print("Hello " + input("What is your name?"))

# Using a function inside a function
print(len(input("What is your name? ")))