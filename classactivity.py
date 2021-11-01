#1) Write a Python program to count the number of even and odd numbers from a series of numbers.

#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

numbers=(1,2,3,4,5,6,7,8,9)
count=0
countf=0
for X in numbers:
    if X%2==0:
        count+=1
    if X%2!=0:
        countf+=1
print("number of even numbers are",count)
print("number of odd numbers are",countf)        

#2) Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for Y in range(0,7):
    if Y==3 or Y==6:
        continue
    else:
        print(Y)
#4)Create a list and find the largest element in a list using max() function by passing objects as arguments (numbers).
A=[1,2,3,4,5,6,7,8,9]
print(max(A))

#5). Print the sum of the given list.

#  my_list = [10,20,30,40,50,50,60,10]
my_list=[10,20,30,40,50,50,60,10]
print(sum(my_list))

#6)Python function to add two variables values with the following:
#i) with return
def addition(U,V):
    S=U+V
    return S
print(addition(5,9))
#ii)without return
def addition2(D,F):
    P=D+F
    print(P)
addition2(10.464055,15.3259)

#7)Find out the student’s grade from the marks obtained by the student.
a=int(input("Enter Your Obtained marks:"))
if a>=95:
    print("Your Grade is A+")
elif a>=90:
    print("Your Grade is A")
elif a>=85:
    print("Your Grade is B+")
elif a>=70:
    print("Your Grade is B")
elif a>=50:
    print("Your Grade is C")
elif a>=45:
    print("Your Grade is D")
else:
    print("Fail")
#8)Compare two lists in Python and display the corresponding results.
W=[1,2,3,34,5,69,8,14]
Q=[2,1,34,14,8,3,5,69]
W.sort()
Q.sort()
if W==Q:
    print("Compared lists are equal")
else:
    print("Compared lists are not equal")


    
    
    


















