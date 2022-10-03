#1. Create a Python file named lab_3-6.py
#2. Write a statement that creates the string "Fairfield Prep" by
#concatenating substrings.
#3. Write a statement that creates a dashed line that is 20 dashes long.
#4. Write a statement that prints the following:
#    I'm loving this short story I'm reading, "The Fall of the House of Usher"
#5. Write a statement that prints the length of the previous string.
#6. Write a statement using the index operator that returns the "L" in "apple"

#Statement that creates the string "Fairfield Prep" by
#concatenating substrings.

from multiprocessing.pool import ApplyResult


x = 'Fairfield'
y = 'Prep'
concat = x + ' ' + y
print(concat)
 
#statement that creates a dashed line that is 20 dashes long

r = '-'
print(r * 20)

#Write a statement that prints the following:
#    I'm loving this short story I'm reading, "The Fall of the House of Usher"
f = 'I\'m loving this short story I\'m reading, "The Fall of the House of Usher"'
print(f)

#Statement that prints the length of the previous string.
print(len(f))

#Statement using the index operator that returns the "L" in "apple"
XIA = 'apple'
print(XIA[3])