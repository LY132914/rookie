def cnt(l1):
    l= {}
    for i in range(len(l1)):
        if l1[i] in l:
            l[l1[i]]+=1
        else:
            l[l1[i]]=1
    return l
num=[1,2,3,3,3,4,4,4,4,4,5,5,6,6,6]
print(cnt(num))