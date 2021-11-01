#swapping using third variable 
A=int(input("Enter 1 st number:"))
B=int(input("Enter 2 nd number:"))
print("befpore swapping",A,B)
temp=A
A=B
B=temp
print("after swapping",A,B)
#swapping using arithmetic operators
X=int(input("Enter 1 st number:"))
Y=int(input("Enter 2nd number:"))
print("before swapping",X,Y)
(X,Y)=(Y,X)
print("after swapping",X,Y)
W=int(input("Enter 1st number:"))
D=int(input("Enter 2nd number:"))
print("before swapping",W,D)
W=W-D
D=W+D
W=D-W
print("after swapping",W,D)
P=int(input("Enter 1st nmber:"))
Q=int(input("Enter 2nd number:"))
print("before swapping",P,Q)
P=P*Q
Q=P/Q
P=P/Q
print("after swapping",P,Q)
#swapping using bitwise operator(XOR)
E=int(input("Enter 1st number:"))
F=int(input("Enter 2nd number:"))
print("before swapping",E,F)
F=E^F
E=E^F
F=E^F
print("after swapping",E,F)
