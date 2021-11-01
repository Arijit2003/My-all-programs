#1)
A=int(input("Enter RS:"))
D=A/74.73
print(A,"in $ is",D)
def dollar_from_RS(B):
    D=B/74.73
    return D
F=int(input("Enter RS:"))
print(dollar_from_RS(F))

def Rs_to_dollar(a):
    dollar=a/74.73
    print(dollar)
r=int(input("Enter Rs:"))
Rs_to_dollar(r)
#2)
A=input("Enter Character:")
print("The ASCSII value",ord(A))

#3)
X=0
Y=1
while X<=100:
    print(X)
    (X,Y)=(Y,X+Y)


#4)Factorial
def factorial(A):
    mul=1
    for X in range(1,A+1):
        mul=mul*X
    print("factorial of",A,"is",mul)
factorial(int(input("Enter any number:")))
#Program on Control Flow (Conditional & Loops)
#1)
A=int(input("Enter Number:"))
i=0
Sum=0
for X in str(A):
    W=int(X)*10**i
    Sum=Sum+W
    i=i+1
print(Sum)
#2)

A=int(input("Enter Number:"))
if A>0:
    print("The number is positive.")
elif A<0:
    print("The number is negative.")
else:
    print("The number is",0)


#Program on Functions


#1)
def maximum(a,b,c):
    if a>b and a>c:
        print(a,"is the maximum")
    elif b>a and b>c :
        print(b,"is the maximum")
    else:
        print(c,"is the maximum")
    
maximum(10,15,24)

#2)
A=[1,2,3,4,5,6,78,9,8]
mul=1
for X in A:
    mul=mul*X
print(mul)

#3)
def unique_list(a):
    S=set((a))
    L=list((S))
    L.sort()
    print(L)
unique_list([1,2,3,4,1,2,5,9,8,7,8])

#4)
def multiplication():
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    def multiplication2(c,d):
        D=c*d
        print(D)
    multiplication2(a,b)
multiplication()

#5)
def square(num):
    D=num**2
    return D
def cube(num2):
    J=num2**3
    return J
A=[1,2,3,4,5,6,7,8,9]
B=(1,20,3,40,54,6,79.9,8,9)
C={1,2.5,3,4,0.5,67.336,7,81,92}
print(list(map(square,A)))
print(set(map(cube,B)))
print(tuple(map(square,C)))
squ=lambda X:X**2
cube1=lambda Y:Y**3
print(list(map(cube1,A)))
print(tuple(map(squ,B)))





















