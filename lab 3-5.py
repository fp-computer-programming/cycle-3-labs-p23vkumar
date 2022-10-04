#1. Create a Python file named lab_3-5.py
#2. Import the time and math modules.
#3. Calculate 22 using math.pow and again using the ** operator.
#4. Record the time using time.process_time before and after each
# calculation (Hint: you may need to store the result of time.process_time 
# in a variable)
#5. Add a statement that prints the elapsed time after each statement 
# is processed. Run the program. What do you notice?
#6. Change each statement that records the time to use time.perf_counter
#  instead of time.process_time.
#7. Run the program again. What do you notice?

#Import the time and math modules.
import time
import math 

#Calculate 22 using math.pow and again using the ** operator.
x = math.pow(2, 2)
print(x)
y = 2 ** 2 
print(y)

#Record the time using time.process_time before and after each
#calculation (Hint: you may need to store the result of time.process_time 
# in a variable)

z = time.process_time()
print(z)

#5. Add a statement that prints the elapsed time after each statement 
# is processed. Run the program. What do you notice?

w = time.process_time()
print(w)
#This time statement changes before and after the statement is printed since 
#its gives the highest resolution to measure a short duration 

#6. Change each statement that records the time to use time.perf_counter
#  instead of time.process_time.
#7. Run the program again. What do you notice?
d = time.perf_counter()
print(d)
##Similar to the time.pricess_time()
# the time statement changes before and after the statement is printed since 
#its gives the highest resolution to measure a short duration 