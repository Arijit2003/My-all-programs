i=0
while i<5:
    U=False
    L=False
    D=False
    S=False
    A=input("Enter Strong Password:")
    if len(A)>6 or len(A)<16:
        for X in A:
            if X.isupper():
                U=True
            if X.islower():
                L=True
            if X.isdigit():
                D=True
            if X=="@" or X=="#" or X=="$":
                S=True
        if U==True and L==True and D==True and S==True:
            print("Your password is strong")
            break
        else:
            print("Invalid Password")
    else:
        print("Your Password must contain 6-16 characters")
    i=i+1
    
        
            
            
    
