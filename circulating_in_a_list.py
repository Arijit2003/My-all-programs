def circulate(list,n):
    print(list)
    list=list[n:]+list[:n]
    print(list)
circulate([1,2,3,4,5,6,7,8,9],-2)
