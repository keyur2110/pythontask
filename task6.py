# Exercise-1
x = 'ABcdEfG'
l =[i for i in x if i.isupper()]
print(l)

# Exercise-2
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
new_dic = {}
for i,j in zip(students,subjects):
    new_dic[i]=j
print(new_dic)

# Exercise-4
def fun(s):
    for i in range(len(s)-1,-1,-1):
        yield s[i]

for i in fun("Consultadd Training"):
    print(i)



# Exercise-5  
def dec(func):
    def inner(a,b):
        print(f"addition of {a} and {b}:")
        return func(a,b)
    return inner

@dec
def addition(a,b):
    print(a+b)
addition(5,5)
addition(9,18)

