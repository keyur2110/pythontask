# Exercise-1
import math
C = 50
H = 30
D = input("Enter the values of D separated by comma: ")

x = D.split(",")
l =[]
for d in x:
    q = math.sqrt(2*C*int(d)/H)
    l.append(q)
print(l)

# Exercise-2
class Shape():
    def area(self):
        print("Area is",0)
        return None

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print("Area is",self.length*self.length)
        return None

# Exercise-3
l = [-25,-10,-7,-3,2,4,8,10]
class sum3():
    def __init__(self,l):
        self.l = l
    def sum(self):  
        x=[]
        for i in range(0,len(l)-2):
            for j in range(i+1,len(l)-1):
                for k in range(j+1,len(l)):
                    if l[i] + l[j] + l[k] == 0:
                        x.append([l[i],l[j],l[k]])
                           
        print(x)    
        return None
    
s = sum3(l)
s.sum()
              
# Exercise-4
class time():
    def __init__(self,hour,minute):
        self.hour=hour
        self.minute = minute
    
    def addtime(self,a,b):
        total_minutes = a.minute + b.minute
        hours,minutes = divmod(total_minutes,60)
        total_hour = a.hour+b.hour+hours
        return time(total_hour,minutes)        

    def displaytime(self):
        print(f"{self.hour} hr {self.minute} min")
    def displayminutes(self):
        total_minutes = (self.hour*60)+self.minute
        print(total_minutes)

o1 = time(1,40)
o2 = time(4,40)
o3 = o1.addtime(o1,o2)
o3.displaytime()
o3.displayminutes()
        
            
class person():
    def __init__(self,age):
        if age <0:
            self.age=0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = age
            # print(self.age)
    
    def yearsPasses(self,years):
        self.years = years
        self.age +=self.years
        return self.age
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age>=13 and self.age<=19:
            print("Yor are teenager.")
        else:
            print("You are old.")
    
p = person(38)
print(p.yearsPasses(4))
p.amIOld()
p1 = person(-2)
print(p1.yearsPasses(94))
p1.amIOld()
p2 = person(4)
p2.yearsPasses(10)
p2.amIOld()