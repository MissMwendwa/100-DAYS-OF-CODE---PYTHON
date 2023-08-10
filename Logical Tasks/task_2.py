# This is the second equation
#Create my variables
# P for T and Q for F

p = True
q = False

# First part of the Eq.
var_1 = p or q

# the second part
var_2 = p or (not q)

# Answer
ans = var_1 and var_2
print(ans)