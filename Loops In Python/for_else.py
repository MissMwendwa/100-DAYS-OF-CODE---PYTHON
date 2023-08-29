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
'''for i in food:
    exhausted = exhausted - 1
    if(exhausted > 3):
        print("You can buy food")
    else:
        print("Go to the kitchen and cook")

else:
    if(guest >= 5):
        print("Go buy some food!")
    else:
        print("Go to prepare some food.")'''


# Case study Goal is to wake up early in the morning
#var = sickness
#var 2 = poverty
#var 3 = work
#var 4 = Preparation
#var 5 = school
#var 6 = Devotion
#var 7 = vacation


#The for() block will represent work and then the else() block will represent vacation
work = 5
vacation = 2
day = 0

#for Block() starts here
'''for i in range(work):
    day = day + 1
    if (day <= work):
        print("wake up early in the morning!")
    else:
        print("You can sleep in")
    print("The day is:  ", day)

else:
    day = day + 6
    if (day > work):
        print("You can wake up late!")
    else:
        print("You can wake up early")'''


#Case study 3 complex For()...Else() loop
my_list = [1, 23, 34, 15, 17, 18, 37, 45, 21, 2]
patt = "x"

#for() Block starts
for i in my_list:
    if(i < 45):
        patt = patt * 9
        print(patt)
    elif(i < 37):
        patt = patt *8
        print(patt)
    elif(i < 34):
        patt = patt *7
        print(patt)
    elif(i < 23):
        patt = patt *6
        print(patt)
    elif(i < 21):
        patt = patt * 5
        print(patt)
    elif(i < 18):
        patt = patt * 4
        print(patt)
    elif(i < 17 ):
        patt = patt *3
        print(patt)
    elif(i < 15):
        patt = patt * 2
        print(patt)
    elif(i < 2):
        patt = patt * 1
        print(patt)
    else:
        patt = patt *0
        print(patt)

else:
    if(i <= 45):
        print(my_list)
    else:
        print(patt)

