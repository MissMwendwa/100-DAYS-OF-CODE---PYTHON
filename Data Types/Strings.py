# This will be the first Data Type we Cover
# We will be performing both operations and creating strings

# First Part
var_str = ' My name is Alice'
var_str2 = " My name is Shadrack"

# Print Operations
#print(var_str)
#print(var_str2)

#Methods
# Length of the string
print(len(var_str))
print(len(var_str2))

# Upper Operation
var = var_str.upper()
#print(var)

var_2 = var_str2.upper()
#print(var_2)


# Lowercase
low = var_str.lower()
low_2 = var_str2.lower()

#print(low, low_2)

# Split Method
spl = var_str.split()
print(spl)

spl2 = var_str2.split()
print(spl2)

#Replace Method
a = "team"
b = a.replace("team", "mangoes")

#print(b)

# Using the Statements
var_str = 'My name is Alice'
var_rep = var_str.replace('My name is Alice', " I have an Avocado")

#print(var_rep)

# Strip Method
# strip()

var_st = var_rep.strip()
print(var_st)

