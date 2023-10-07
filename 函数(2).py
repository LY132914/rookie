def cnt(l1):
    l= {}
    for i in l1:
        if i in l:
            l[i]+=1
        else:
            l[i]=1
    return l
num=[1,2,3,3,3,4,4,4,4,4,5,5,6,6,6]
print(cnt(num))
