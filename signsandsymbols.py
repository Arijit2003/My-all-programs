print(4*"*")
i=0
while i<=10:
    print(i*"*")
    i+=1

j=10
while j>0:
    print(j*"*")
    j=j-1


l=int(input("Enter no."))
b=1
X=l*" * "
while b<l:
    print(X.center(20))
    b=b+1

import re    
T=True
while T:
    A=input("Enter a strong Password:")
    if len(A)<6 and len(A)>16:
        print("Your password must be within 6-16 characters")
        print("Create again")
        continue
    if not re.search("[a-z]",A):
        print("Invalid Password")
        print("Create again")
        continue
    if not re.search("[A-Z]",A):
        print("Invalid Password")
        print("Create again")
        continue
    if not re.search("[0-9]",A):
        print("Invalid Password")
        print("Create again")
        continue
    if not re.search("[@#$]",A):
        print("Invalid Password)
        print("Create again")
        continue
    else:
        print("Its a strong password")
        break
