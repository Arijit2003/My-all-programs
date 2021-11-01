A=input("Enter any word:")
print(A[::-1])
#1) using third variable
C=int(input("Enter 1st number:"))
D=int(input("Enter 2nd number:"))
print("Before swapping",C)
print("Before Swapping",D)
temp=C
C=D
D=temp
print("After swapping",C)
print("After swapping",D)
#2) using tuple assignment
E=int(input("Enter 1st number:"))
F=int(input("Enter 2nd number:"))
print("Before swapping",E)
print("Before Swapping",F)
(E,F)=(F,E)
print("After Swapping",E)
print("After swapping",F)
#3) Arithmetic operators
#using + and -
G=int(input("Enter 1st number:"))
H=int(input("Enter 2nd number:"))
print("Before Swapping",G)
print("Before Swapping",H)
G=G+H
H=G-H
G=G-H
print("After Swapping",G)
print("After Swapping",H)
# using * and /
I=int(input("Enter 1st number:"))
J=int(input("Enter 2nd number:"))
print("Before Swapping",I)
print("Before Swapping",J)
I=I*J
J=I/J
I=I/J
print("After Swapping",I)
print("After Swapping",J)
#4)using Bitwise operator
# Bitwise XOR (^)
K=int(input("Enter 1st num:"))
L=int(input("Enter 2nd numb:"))
print("Before swapping",E)
print("Before Swapping",F)
K=K^L
L=K^L
K=K^L
print("After Swapping",K)
print("After Swapping",L)
Sum=0
j=True
i=0
while j==True:
    i=i+1
    if i<=4:
        j=True
        A=int(input("Enter Num:"))
        Sum=Sum+A
    else:
        j=False
print(Sum)
if Sum>100:
    print("Yes its greater than 100")
else:
    print("Its not greater than 100")


i=0
while True and i<4:
    i+=1
    A=int(input("Enter num1:"))
    if A>100:
        continue
    print(A)
    

i=0
while True:
    i=i+1
    if i>10:
        break
    else:
        print(i)
A=[1,2,3,4,5,6,7]
for X in A:
    if X==7:
        continue
    else:
        print(X)

for X in A:
    if X==6:
        break
    else:
        print(X)

A=[1,2,3,4,5,6,6,4,7,8]
i=0
while i<=len(A)-1:
    for X in A:
        if A.index(X)==i:
            continue
        elif A[i]==X:
            print(X,"is the duplicate member")
            break
    i=i+1

count=1
i=0
while i<=len(A)-1:
    for X in A:
        if A.index(X)==i:
            continue
        elif A[i]==X:
            count=count+1
    print(A[i],"is repeated",count,"times")
    i=i+1



























































