#1. Create a Python file named lab_3-3.py
#2. Import the random module.
#3. Use the randint() function to generate a random 
# integer between 1 and 100.
#4. Compare your result with another classmate. 
# What do you notice about the results?
#5. Use the seed() function to set the random seed to a value 
# that you and a classmate agree on.
#6. Use the randrange() function to generate an even number 
# between 0 and 100.
#7. Compare your result with your classmate. 
# What do you notice about the results?

#Import the random module.
import random
from re import X

#Use the randint() function to generate a random integer between 1 and 100.
Delta = random.randint(1, 100)
print(Delta)

#Compare your result with another classmate. 
# What do you notice about the results?
print("The result seem to be a random generated number between the range of 1 to a 100")

#5. Use the seed() function to set the random seed to a value 
# that you and a classmate agree on.

x = int(input("Enter Number: "))
random.seed(X)
print(random.random())

#6. Use the randrange() function to generate an even number 
# between 0 and 100.
#7. Compare your result with your classmate. 
# What do you notice about the results?
random.randrange(0, 100, 2)
print(random.randrange(0, 100, 2))
print("The output is 94 and this is the only number that seems to be displayed in the terminal")
