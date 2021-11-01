def circulation(list,n):
    print(list)
    print("left circulation by 3")
    list=list[n:]+list[:n]
    print(list)
circulation([1,2,True,2.5,"Hero",[3,4,56,58],("a","b","c"),{100,200,300},{"cars":"tesla","fruit":"mango"}],3)
def circulation1(A,B):
     print(A)
     print("right circulation by 3")
     A=A[B:]+A[:B]
     print(A)
circulation1([1,2,True,2.5,"Hero",[3,4,56,58],("a","b","c"),{100,200,300},{"cars":"tesla","fruit":"mango"}],-3)
