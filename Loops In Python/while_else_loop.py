# This is the first while loop() having a break from repetition
# Its kind of a simple-complex while loop for the interprater
# We'll have 3 examples

#Case Fruit shopping
# bananas = 300, oranges=400, 1500

shopping_bg = 1500
bananas = 0 
oranges = 0

#Decreasing while loop()
while(shopping_bg >= 900):
    shopping_bg = shopping_bg - 300
    print("The amount Remaining is: ",shopping_bg )
    bananas = bananas + 20
    print("The bananas I have bought are: ", bananas)
else:
    oranges = oranges + 30
    print("The oranges I have bought: ", oranges)