# the first logical question
# P for False and Q for True
#Create the first varibles

p = False
q = True

# Creating the first Eq part
var_a = p or q

#Create the 2 part of the Eq.
var_b = (not q) and (not p)

# Combine the Eq.
ans_1 = var_a; (not var_b)
print(ans_1)