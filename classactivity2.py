# with argument with return
def addition(X,Y):
    C=X+Y
    return C
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
print("addition is",addition(a,b))
def substraction(U,V):
    D=U-V
    return D
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
print("substraction is",substraction(a,b))
def multiplication(X,Y):
    C=X*Y
    return C
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
print("multiplication is",multiplication(a,b))
def division(X,Y):
    C=X/Y
    return C
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
print("division is",division(a,b))
def floor_division(X,Y):
    C=X//Y
    return C
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
print("floor division is",floor_division(a,b))
def modulus(X,Y):
    C=X%Y
    return C
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
print("remainder is",modulus(a,b))


#without return with arguments
def addition(X,Y):
    C=X+Y
    print ("addition is",C)
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
addition(a,b)
def substraction(U,V):
    D=U-V
    print("substraction is",D)
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
substraction(a,b)
def multiplication(X,Y):
    C=X*Y
    print("multiplication is",C)
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
multiplication(a,b)
def division(X,Y):
    C=X/Y
    print("division is",C)
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
division(a,b)
def floor_division(X,Y):
    C=X//Y
    print("floor_division",C)
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
addition(a,b)
def modulus(X,Y):
    C=X%Y
    print("remainder is",C)
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
modulus(a,b)
#without argument without return

def addition():
    X=int(input("Enter 1 st num:"))
    Y=int(input("Enter 2nd num:"))
    C=X+Y
    print("addition is",C)
addition()
def substraction():
    U=int(input("Enter 1st Number"))
    V=int(input("Enter 2nd Number"))
    D=U-V
    print("substraction",D)
addition()
def multiplication():
    X=int(input("Enter 1st Number"))
    Y=int(input("Enter 2nd Number"))
    C=X*Y
    print("multiplication is",C)
multiplication()
def division():
    X=int(input("Enter 1st Number"))
    Y=int(input("Enter 2nd Number"))
    C=X/Y
    print("division is",C)
division()
def floor_division():
    X=int(input("Enter 1st Number"))
    Y=int(input("Enter 2nd Number"))
    C=X//Y
    print("floor_division",C)
floor_division()
def modulus():
    X=int(input("Enter 1st Number"))
    Y=int(input("Enter 2nd Number"))
    C=X%Y
    print("remainder is",C)
modulus()
# without argument with return
def addition():
    X=int(input("Enter 1 st num:"))
    Y=int(input("Enter 2nd num:"))
    C=X+Y
    return C
print("addition is",addition())
def substraction():
    U=int(input("Enter 1st Number"))
    V=int(input("Enter 2nd Number"))
    D=U-V
    return D
print("substraction is",substraction())
def multiplication():
    X=int(input("Enter 1st Number"))
    Y=int(input("Enter 2nd Number"))
    C=X*Y
    return C
ptrint("multiplication is",multiplication())
def division():
    X=int(input("Enter 1st Number"))
    Y=int(input("Enter 2nd Number"))
    C=X/Y
    return C
print("division is",division())
def floor_division():
    X=int(input("Enter 1st Number"))
    Y=int(input("Enter 2nd Number"))
    C=X//Y
    return C
print("floor division is",floor_division())
def modulus():
    X=int(input("Enter 1st Number"))
    Y=int(input("Enter 2nd Number"))
    C=X%Y
    return C
print("remainder is",modulus())

# Without Separate
#with argument with return
def calculator(G,H):
    A=G+H
    S=G-H
    M=G*H
    D=G/H
    FD=G//H
    REMAINDER=G%H
    return A,S,M,D,FD,REMAINDER
a=float(input("Enter 1st num:"))
b=float(input("Enter 2nd num:"))
print(calculator(a,b))

# with argument without return
def calculator_2 (P,Q):
    print("Addition is",P+Q)
    print("Substraction",P-Q)
    print("Multiplication is",P*Q)
    print("Division is",P/Q)
    print("Floor division is",P//Q)
    print("Remainder is",P%Q)
a=int(input("Enter 1st num:"))
b=int(intput("Enter 2nd num:"))
calculator_2(a,b)

#without argument with return

def calculator_3():
    G=int(input("Enter 1st num:"))
    H=int(input("Enter 2nd num:"))
    A=G+H
    S=G-H
    M=G*H
    D=G/H
    FD=G//H
    REMAINDER=G%H
    return A,S,M,D,FD,REMAINDER
print(calculator_3())

#without argument without return


def calculator_4():
    P=int(input("Enter 1st num:"))
    Q=int(input("Enter 2nd num:"))
    print("Addition is",P+Q)
    print("Substraction",P-Q)
    print("Multiplication is",P*Q)
    print("Division is",P/Q)
    print("Floor division is",P//Q)
    print("Remainder is",P%Q)
calculator_4()
    



















