# the first logical question
# P for True and Q for False
#Create the first varibles

p = True
q = False

# Creating the first Eq part
var_a = p or q

#Create the 2 part of the Eq.
var_b = (not q) and (not p)

# Combine the Eq.
ans_1 = var_a; (not var_b)
print(ans_1)