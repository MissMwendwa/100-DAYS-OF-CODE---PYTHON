# Bit Operations 
# 3 menthods of Bit Operations
# In each method, we will use 2 Concepts
# We will use user-defined Functions
# We will use Program Built functions

# METHOD 1
# The inbuilt Function is DecimalToBinary()
# bin()

# User Defined function
# def ...():
#      return()

#DecimalToBinary
def DecimalToBinary(num):   # Function Definition
    return("{0:b}".format(int(num)))

#Funct Calling
d = DecimalToBinary(9) 
#print(d)

#Func call 2
s = DecimalToBinary(546)
#print(s) 


#Bin Function
t = bin(14) # Quick Ninja way
#print(t)

#Second Escapade
r = bin(789)
print(r)