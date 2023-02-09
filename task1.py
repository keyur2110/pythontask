# # Exercise-1
a,b,c =1,"string", True

# #Exercise-2
a = 1+2j
b = 2
print(f"a:{a}, b :{b}")
a,b= b,a
print(f"a:{a}, b :{b}")

# #Exercise-3
x1 = 1
y1 = 2
# # With third variable
temp = x1
x1 = y1
y1 = temp
# # without Third variable
x,y = 1,2
x = x + y
y = x-y
x = x-y

# Exercise-4
x = input("enter something.\n")
print(x)
print "x"

# Exercise-5
num1 = int(input("Enter number 1 between (1-10): "))
num2 = int(input("Enter number 2 between (1-10): "))
z = num1 + num2
result = z + 30
print(result)

# Exercise-6
y = input("Enter a value: ")
try:
    if type(eval(y))== float:
        print("Datatype is float. ")
    elif type(eval(y))== int:
        print("Datatype is int.")
    elif type(eval(y))== bool:
        print("datatype is boolean.")
except:
    print("Datatype is stringsss.")

# Exercise 7
x = 'keyur patel'
UpperCamelCase = 'KeyurPatel'
LowerCamelCase = 'keyurPatel'
SnakeCase ='keyur_patel'
UPPERCASE = 'KEYUR PATEL'

# Exercise 8
"""if we assign one datatype value to a variable and then again assign different datatype value to a same variable it will changed the value to a new datatype.
new datatype value will override the old value."""
a = 'keyur'
print(a)
a = 10
print(f"changed value:{a}")