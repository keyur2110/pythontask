# Exercise-1
s = "abcd"
print(s[::-1])

# Exercise-2
s1 = "ABCdehGHtsjZXZS"
u,l=0,0
for i in s1:
    if i.isupper()==True:
        u+=1
    else:
        l+=1
print(f"uppercase: {u} and lowercase: {l}")

# Exercise-3
l=[1,2,2,3,3,4,4,5,6,7,8,8,8,9,10,10]
t = set(l)
l1 = list(t)
print(l1)
    
# Exercise-4
s4 = input("enter words separated by hyphen:\n")
l4 = s4.split("-")
l4.sort()
s = '-'.join(l4)
print(s)

# Exercise-5
s5 = input("Enter a line\n")
s_cap = ''
for i in s5:
    s_cap += i.capitalize()
print(s_cap)

# Exercise-6
def fun():
    numbers = input("enter two number separated by space: ")
    l = numbers.split(' ')
    sum = int(l[0])+int(l[1])
    # print(sum)
    return sum
print(fun())

# Exercise-7
def fun2():
    string1 = input("enter string1: ")
    string2 = input("enter string2: ")
    if len(string1)>len(string2):
        print(string1)
    elif len(string1)<len(string2):
        print(string2)
    else:
        print("Both strings are same..")
    return None
fun2()

# Exercise-8
def fun3():
    l = []
    for i in range(1,21):
        l.append(i**2)
    t = tuple(l)
    print(t)
    return None
fun3()

# Exercise-9
def shownumbers(number):
    for i in range(0,number+1):
        if i %2 == 0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")
    return None
shownumbers(3)

# Exercise-10
l = [*range(0,21)]
l10 = list(filter(lambda x:x%2==0,l))
print(l10)

# Exercise-11
l11 = [1,2,3,4,5,6,7,8,9,10]
f_list = list(filter(lambda x:x%2==0,l11))
final = list(map(lambda x:x**2,f_list))
print(final)

# Exercise-12
def fun():
    try:
        print(5/0)
    except:
        print("Cannot divide by zero.") 
    return None
fun()

# Exercise-13
import functools
def func(*l):
    st = ''
    for i in l:
        st+=str(i)
    return st
lis = [1,2,3,4,5,6,7]
l13 = functools.reduce(func,lis)
print(l13)
  
# Exercise-14  
def fun3(a):
    if a % 3 !=0:
        result = a
    def fun7(b):
        if b % 7 ==0:
            return b
    return fun7(result)

# Exercise-15
def fun(l):
    return l*l
l15 = [1,2,3,4,5]  
new_l15 = list(map(fun,l15))
print(new_l15)

# Exercise-16
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)
"""
Output : 2
"""

# def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#         print('after f?')
# a()
"""
Output :
after f
after f?
"""   
    
    