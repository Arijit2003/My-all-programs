A=[1,2,3,4,5,6,6,4,7,8,3]
i=0
while i<=len(A)-1:
    for X in A:
        if A.index(X)==i:
            continue
        elif A[i]==X:
            print(X,"is the duplicate member")
            break
    i=i+1

A=[1,2,3,4,5,6,4,8,1,7,8,9,9,5,2]
S=[]
for i in A:
    if i not in S:
        S.append(i)
    else:
        print("duplicate members are",i)
N=[1,2,3,4,5,6]
def LIST(a,n):
    a=a[n:]+a[:n]
    print(a)
LIST([1,2,"a","b",3,4,"c","d"],2)


