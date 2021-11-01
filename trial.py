#def maximum(a,b,c):
#    if a>b and a>c:
#        return a
#    elif b>a and b>c:
#        return b
#    else:
#        return c
#print(maximum(1,15,14))
#
#def multiplication():
#    a=int(input("Enter 1st number:"))
#    b=int(input("Enter 2nd number:"))
#    def multiplication2(c,d):
#        D=c*d
#        print(D)
#    multiplication2(a,b)
#multiplication()
#def even_or_not(num):
#    if num%2==0:
#        print(num,"is even")
#    else:
#        print(num,"is odd")
#A=[1,2,3,4,5,6]
#tuple(map(even_or_not,A)) 
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
#W=squ(10)
#print(W)
cube1=lambda Y:Y**3
print(list(map(cube1,A)))
print(tuple(map(squ,B)))
