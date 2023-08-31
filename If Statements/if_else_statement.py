# This is the 2-1 decision if
# It only represent one decision to be made
# the syntax looks something like this
#if (criteria):
#    statement/execution
#else:
#    statement/exection

#Lets write some code
# school scenarion
math = 85
phy = 80
eng = 78
chem = 82
marks = (math+phy+eng+chem)

# if section
#if(marks >= 280):
    #print(math)
    #print(phy)
#else:
#    print(eng)

#House hunting
hse_a = 10000
hse_b = 15000
budget = 12000

#if section
#if (budget > 12000):
#    print(hse_a)
#    print("House price is within the budget")
#else:
#    print(hse_b)
#    print("House is too expensive")


# Baby Feeding scenario
baby_age = "8 months"

# If section
#if (baby_age >= "1 year"):
#    print("You can stop breast-feeding")
#    print(" You can give them cow milk")
#else:
#    print("Breast milk is a must")
#    print(" The baby is still weaning")


# Moving out Scenario
school_dis = "Near"
desire = "No freedom"

#if Section
if(school_dis == "far" or desire == "freedom"):
    print("We are moving Out!")
else:
    print("Stay with your parents")