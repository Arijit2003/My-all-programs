A=[1,2,3,4,5,6,4,5,6,6,4]
B=[]
C=[]
for X in A:
    if X not in B:
        B.append(X)
    else:
        C.append(X)
D=set(C)
E=list(D)
E.sort()
for G in E:
    print("Duplicate members are",G)
for Z in E:
    count=0
    for ele in A:
        if ele==Z:
            count+=1
    print(Z,"occurs in the list",count,"times")
    

