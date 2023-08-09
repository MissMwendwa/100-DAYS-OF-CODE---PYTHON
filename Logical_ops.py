#This is a logical operations file
# I'm performing basic logical operations for demonstartion

#Logical OR
var_1 = 24
var_2 = 30

var = var_1 or var_2
#print(var)

#Logical AND
var_3 = var_1 and var_2
#print(var_3)

#Logical NOT
var_4 = not var_2
#print(var_4)


char_1 = True
char_2 = False

#Logical OR
char = char_1 or char_2
#print(char)

#New set of examples of logical operators
# OR Test Run
x = True
y = False

var_o = x or y
var_c = y or y
#print(var_o)
#print(var_c)

#AND Test Run
var_a  = x and y
var_b = x and x
#print(var_b)

#NOT Test run
var_t = not y
var_f = not x

#print(var_f)
#print(var_t)

#Demonstration of using Logical Operations
p = True
q = False

#Demonstration 01
var_q = p or (not q) #p and negative q
var_s = (not p) and q # negative p and q
ans = var_q and var_s  # full represantation of the question
#print(ans) # print my ans

# Demonstration 02
p = True
q = False
#r = True

# create segments of the questions
var_p = p or q #True
#var_q = r or (not q) #True

var_a1 = (var_p and var_q)

#var_r = p or r #True

#full operation
#answer_2 = var_a1 and (not var_r)
#print(answer_2)

# Question One
p = True
q = False
r = False

# Query 01
var_d = (not p) or (not q)
var_a2 = var_d and r

#query 02
var_i = q and (not r)

#ans
ans_1 = var_a2 or var_1
print(ans)


#Question 02
#query 01
var_r1 = p or q
var_r2 = var_r1 and r

#query 02
var_r3 = p and r
var_r4 = q and r
var_r5 = var_r3 and var_r4

#answer
ans_02 = var_r2 or var_r5
print(ans_02)






