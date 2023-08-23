# This is a codelab to perform looping using while()
# This is a normal while loop()
#We'll have 3 Examples for better understanding

#syntax
'''while(condition):
    repetitive task
    statement/s'''

# Case Grocery shopping

#milk = 10 (preffered condition)
'''milk = 2

#while loop starts here
while(milk < 10):
    milk = milk + 1
    print("Purchase some more milk")'''

# Case study 2
# Vacation
#budget = 14000  (Preffered Condition)
#save = 3000        (for this to happen)
'''counter = 5
budget = 13500
save = 3000

#while()starts here
while(budget <= 15000 and counter <= 5):
    save = save + 3000
    counter = counter + 1
    print(save)'''

#Case 3 Tap example
# Pressure = 35 max_opens = 8

pressure = 15
max_opens = 3
 #a != A
# While loop()
while (pressure < 35 and max_opens < 8):
    pressure = pressure + 5
    max_opens = max_opens + 1
    print(" The pressure is: ", pressure)
    print("The tap is opened only: ", max_opens)