#This is a try exception handling file
#It will demonstrate the use of the Try statements
#Works in error handling

#First demonstration
var_a = 34
var_b = "daisies"

#Try() block starts here
try:
    calc = var_a + var_b
    print(calc)
except:
    print("An error has occured")


#Second demonstration
#Perimeter, area and Volume of a rectangle shape

length = 14
heighT = 13
width = 8

#Try()Block starts here
try:
    per = 2*(length + width)
    area = length * width
    vol = area * height

    #print findings 
    print(per)
    print(area)
    print(vol)

except:
    print("The operations has an error")


#Error handling demonstration 3
#Control Structure Other(simple structure)

#variables
situation = "Home alone"

#Control structure starts here

#try:
if (situation == "Home alone"):
    try:
        dec_1 = print("Go out and wear some nice shoes")
        dec_2 = print("Stay home and wear flipflops")
        final = dec_1 or dec_2
        print(final)
    except:
        print("There is an error")
else:
   try:
        print("You are at work look descent!")
   except:
        print("There is an error")

        
        print("There is an error")

#except:
    #print("There is an error")


#Second control structure demonstration
#Logical control structure - 3 decisions

#Varibles(1 true then 0 rep false)
sugar = 1
milk = 1
tea_bags = 0
heat = 1
sufuria = 1
water = 1
sieve = 1

#Control structure starts
try:
    if(sieve == 1 and sufuria == 1 and heat == 1):
        try:
            if(water == 1 and milk == 1):
                try:
                    if(sugar == 1 or tea_bags == 1):
                        try:
                            print("You can cook tea")
                        except:
                            print("An error has occured")
                    else:
                        try:
                            print("You can go buy some necessities")
                        except:
                            print("an error has occured")
                except:
                    print("An error has occured")
        except:
            print("An error has occured")
except:
    print("There is an error in your code")





