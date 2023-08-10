# This is the second equation
#Create my variables
# P for F and Q for T

p = False
q = True

# First part of the Eq.
var_1 = p or q

# the second part
var_2 = p or (not q)

# Answer
ans = var_1 and var_2
print(ans)