# Exercise-1
l1 = ['keyur',123,13+5j,True,[1,2,3,4],'patel',56.23,False,'abc',58]


# Exercise-2
l = [10,11,12,15,14]
print(l[2:5])
print(l[::-1])

l2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Exercise-3
sum = 0
mul = 1
for i in l2:
    sum+=i
    mul*=i
print(f"sum: {sum} and mul:{mul}")

# Exercise-4
print(max(l2))
print(min(l2))

# Exercise-5
newlist = []
for i in l2:
    if i%2!=0:
        newlist.append(i)
print(newlist)

# Exercise-6
squarelist = []
for i in range (1,31):
    if i < 6 or i > 25:
        squarelist.append(i**2)
print(squarelist)


# Exercise-7
l3 = [1,2,3,4]
l4 = [10,11,12,13]
l3[-1:]=l4
print(l3)

# Exercise-8
a={1:10,2:20}
b={3:30,4:40}
c = a | b
print(c)

# Exercise-9
x = int(input("enter a digit:\n"))
di = {}
for i in range(1,x+1):
    di[i]=i**2
print(di)

# Exercise-10
s = input("enter sequence of number separated by ',': ")
li = s.split(",")
tu = tuple(li)
print(li)
print(tu)