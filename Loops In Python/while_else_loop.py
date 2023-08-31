# This is the first while loop() having a break from repetition
# Its kind of a simple-complex while loop for the interprater
# We'll have 3 examples

#Case Fruit shopping
# bananas = 300, oranges=400, 1500

shopping_bg = 1500
bananas = 0 
oranges = 0

#Decreasing while loop()
'''while(shopping_bg >= 900):
    shopping_bg = shopping_bg - 300
    print("The amount Remaining is: ",shopping_bg )
    bananas = bananas + 20
    print("The bananas I have bought are: ", bananas)
else:
    oranges = oranges + 30
    print("The oranges I have bought: ", oranges)'''

# Case study 2
# showering case instance
# desired instance is taking a shower = 1
shower = 1
work = 1
laziness = 1
interview = 1
no_of_showers = 2

#while loop structure
''''while(shower == 1 and no_of_showers > 2):
    
    if(work == 1 and laziness == 1):
        if(interview == 1):
            print("Go take a shower!")
        else:
            print("You can decide not to take a shower")
    else:
        print("Shower and Stay in the house")
    

else:
    if(laziness == 1 and interview == 1):
        if(shower == 1):
            print("Go take a shower.")
        else:
            print("Stay untidy")
    else:
        print("Become a couch potato")
no_of_showers = no_of_showers + 1 '''


# Case study 3
# withdrawal condition , bal > 1000

# time
time = "morning"
bal = 400
location = "Nairobi"
withdrwl_amt = 500
max_amt = 1500
deposit = 2500


#while ()structure
while(bal <= 1000 and location == "Nairobi"):
    if(bal < 1000):
      bal = bal + deposit
      print(bal)
      
    elif(bal > 1000):
      bal = bal - withdrwl_amt
      print(bal)
      print("You have withdrawn.")

else:
   print(" You can withdraw after depositing")


