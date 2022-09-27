#2. Copy the following examples into a Python file one at a time. 
# Think about what kind of error you think it will throw before 
# running the code. When you have run one line, be 
# sure to comment it before adding your next line.
# After you have commented out a line, add a comment
# listing what error type occured

#---------------------------------------------------------------------

int(a)
#I think its going to be a value error because it is a 
#letter that cannot be
#within an integer function

#Type of Error: Name Error - Value of a is Not Defined

#---------------------------------------------------------------------

int('a')
# Similar to the first example, this is gonna be a Value 
# Error because the function's argument is of an incorrect
# Type  

#Type of Error: Value Error: Invalid Literal for int() with base 10: 'a'

#---------------------------------------------------------------------

'a' + 2
#This is going to be a Type Error because according 
# the operation that is applied to the function is of an 
#incorrect type

#Type of Error: Can only concatenate str (not "int") to str

#---------------------------------------------------------------------

import date
#This is going to be a Module Not Found Eror
# This is thrown when a module is not found

#Type of Error: ModuleNotFoundError - No Module named 'Date'

#---------------------------------------------------------------------

print("I'm a happy camper!)
#This going to be a Syntax Error since the issue with the 
#structure of the statement is that there is a missing parentheses
#There are missing characters in the print statement 

#Type of Error: Syntax Error: Unterminated String Literal 