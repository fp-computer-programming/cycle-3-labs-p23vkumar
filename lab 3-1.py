#In a video game, you can slay the dragon only if your magic strength is 
# 90 or higher and you shield is charged to at least 75. 
# Assume both values will be provided by the user as integers. 
# Modify the code below to form a simpler to understand conditional that 
# uses logical operators.

#--------------------------------------------------------------------------
#Originial Code

#if not ((magic_charge >= 90) and (shield_charge >= 75)):
   #print ("The dragon burns you to a crisp.")
#else:
   #print ("You defeated the dragon! But the princess is in another castle.")

#----------------------------------------------------------------------------

#New Code

magic_charge = int(input("Enter Number of Points: "))
shield_charge = int(input("Enter Number of Points: "))

if magic_charge >= 90 or  shield_charge >= 75:
   print("The Dragon burns you to a Crisp")
else:
   print("You defeated the dragon! But the princess is in another castle.")