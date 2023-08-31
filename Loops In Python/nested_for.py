#Nested For Loop() codelabs
# We will like 3 Examples
#syntax
'''for iter_var in sequence:
    for iter_var in sequence:
        statement
statement'''


#Case 1: Simple pattern
#We will have 3 parts of the code

#variables
pat = 10
i = 0

#nested For() Incremental pattern
for i in range(0, pat):
    for j in range (0, i+1):
        print("*", end="")
    print()

#Nested For() Decremental pattern
for i in range(0, pat):
    for j in range(i-1, 0):
        print("-", end=" ")
    print()


#ChatGPTs suggestion is correct
for i in range(pat, 0, -1):
    for j in range(1, i+1):
        print("-", end=" ")
    print()


#Intermediate complex example
#Case Brushing your teeth everyday'

#Variables
#toothbrush, toothpaste, baking soda, mirror, water

#Variables
week = 7   #for()
toothpaste = 1
toothbrush = 1
baking_soda = 5 #for()
mirror = 1
water = 7 #for()

#Nested For()
for i in range(0, week):
    for j in range(water):
        for w in range(baking_soda):
            if(toothpaste == 1):
                if(toothbrush == 1):
                    print("You can brush your teeth!")
                else:
                    print("Go buy a new Toothbrush")
            else:
                print("Go buy toothpaste")
        else:
            if(toothpaste == 1 and toothbrush == 1):
                print("Go and Brush your teeth")
                #break

#Case 3: Procedure in dishwashing
#Our Variables
#water, soap, washing brush, dish rack, sink, dishes,

#Variables
period = 7
day = 2
soap = 1
washing_brush = 1
dish_rack = "Empty"
dishes = 1
water = 14

#Nested for()
for i in range(period):
    for d in range(day):
        for w in range(water):
            if (soap == 1):
                if (dishes == 1):
                    if(washing_brush == 1):
                        if(dish_rack == "Empty"):
                            print("Wash your dishes and place them on the dishrack")
                            break
                        else:
                            print("Empty your dish_rack first!")
                    else:
                        print("Go buy a washing brush")
                else:
                    print("You have no dirty dishes")
            else:
                print("Go buy soap")
    else:
        print("You have completed the number of times to wash dishes in a day")






