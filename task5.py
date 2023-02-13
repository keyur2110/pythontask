# Exercise-1
try:
    eval('x===x')
except SyntaxError:
    print("Syntax error :")


# Exercise-2
import sys
filename = sys.argv[1]
while True:
    try:
        f = open(filename,"r")
        print(f.read())
        break
    except FileNotFoundError:
            print("Check the name and enter the name again:")
            filename = input("filename: ")

# Exercise-3
num = input("enter four digit number: ")
if len(num)== 4:
    print(f"number of length four: {num}")
else:
    raise Exception("length is too short/long. Please provide only four digit..")
    
# Exercise-4
user = "keyur"
pwd = "Keyur123"
counter = 4
while counter!=0:
    username = input("User Name: ")
    password = input("Password: ")
    if username ==user and password == pwd:
        print("welcome to website!!!")
        break
    else:
        counter-=1
        if counter!=0:
            print(f"username or password is not matched try again.\n you have {counter} chances..")
        else:
            print("Its Over!!")

# Exercise-6
f = open('doc.txt',"r")
l =  f.readlines()
l2 = [x.replace('\n','') for x in l]
l3 = [x.replace('.','')for x in l2]
x = ' '.join(l3)
st2 = x.split(' ')
for i in st2:
    if len(i)%2==0:
        print(i)
    


    


        
            

 