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
