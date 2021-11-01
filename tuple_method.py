A=(1,3,3,4,6,48,9,4)
print(A)
B=tuple([2,"arijit",True,bin(10),2.5])
print(B)
A=A+(5,)
print(A)
A=A+tuple([20,30,])
print(A)
A=A+B
print(A)
print(A.count(3))
print(A.index(3))
X=len(A)-1
while X>=0:
    if A[X]==3:
        print(X)
    X=X-1
del A
print(A)


