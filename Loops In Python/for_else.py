# This is a two code block looping structure
# The for() loop executes first then the Else() block executed last.
# syntax
'''for x in y:
    statements

else:
    statements'''

#Case study 1: Goal is to not be hungry
#The desired condtions

food = [0, 0, 0] #food is present
exhausted = 3 # if they reach level 5 of exhaustion they will not cook
guest = 5  # this will be part of the else() block


# for...else() block start here
for i in food:
    exhausted = exhausted - 1
    if(exhausted > 3):
        print("You can buy food")
    else:
        print("Go to the kitchen and cook")

else:
    if(guest >= 5):
        print("Go buy some food!")
    else:
        print("Go to prepare some food.")
