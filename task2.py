# Exercise-1
for i in range(1,20):
    if i % 3 ==0 and i % 5 ==0:
        print("Consultadd - Python Training")
    elif i % 3 == 0:
        print("Consultadd")
    elif i % 5 ==0:
        print("Python Training")
    else:
        print(i)

# Exercise-2
print("choose an option from below:\n1)Addition \n2) Subtraction \n3) Division \n4)Multiplication \n5)Average")
choice = int(input("choice: "))
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter Number 2: "))
if choice == 5:
    num3 = int(input("Enter number 3: "))
    num4 = int(input("Enter number 4: "))
result = 0
if choice == 1:
    result = num1 + num2
elif choice ==2:
    result = num1 - num2
elif choice == 3:
    result = num1*num2
elif choice == 4:
    result = num1/num2
else:
    result = (num1+num2+num3+num4)/4

if result<0:
    print("Negative.")
else:
    print(result)
    
# Exercise -3
a = 10
b = 20
c = 30

avg = (a+b+c)/3
print(f"avg: {avg}")
if avg> a and avg >b and avg >c:
    print("average is higher than a,b,c.")
elif avg >a and avg>b:
    print("avg is higher than a and b.")
elif avg > a and avg >c:
    print("avg is higher than a and c.")
elif avg>b and avg >c:
    print("avg is higher than b and c.")
elif avg >a:
    print("avg is just higher than a.")
elif avg >b:
    print("avg is just higher than b.")
elif avg >c:
    print("avg is just higher than c.")

# Exercise-4
while True:
    num = int(input("enter a number: "))
    if num < 0:
        print("It's Over.")
        break
    else:
        print("Good going. ")
        continue

# Exercise-5
for i in range(2000,3200):
    if i % 7 ==0 and i % 5 !=0:
        print(i)

# Exercise-6
# x = 123
# for i in x:
#     print(i)
"""error because x is int"""

# i=0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#     else:
#         print("error")
""" output:
0
error
1
error
2
error
"""
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
"""
0
1
2
3
4
"""

# Exercise-7
for i in range(0,7):
    if i==3 or i ==6:
        continue
    else:
        print(i)

# Exercise-8
s = input("enter something.\n")
lcount=0
ncount=0
for i in s:
    if i.isalpha():
        lcount+=1
    else:
        ncount+=1
print(f"letters {lcount} numbers {ncount}")

# Exercise-9
import random
answer  = random.randint(1,50)
end = "no"
while end=="no":
    number = int(input("guess a number between 1-50: "))
    if answer==number:
        print("Correct guess..")
        end="yes"
    else:
        print("Wrong guess..")
        choice = input("do you want to guess agian? type Y or N. ").capitalize()
        if choice == "Y":
            end = "no"
        else:
            end = "yes"                

# Exercise-10,11
ans = random.randint(1,50)
c = 5
while c>0:
    guess = int(input("enter a guess: "))
    c-=1
    if guess==ans:
        print("Good guess!..")
        break
    else:
        if c !=0:
            print("Try Again..")
        else:
            print("Sorry but that was not successfull.")
print("Game Over..")