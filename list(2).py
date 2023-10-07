l=[]
a=1
while 1:
    a=input()
    l.append(a)
    if a=='-1':
        break
i=0
while True :
    if l[i]=='-1':
        del l[i]
        break
    if str.isalpha(l[i])==1 :
        del l[i]
    else :
        l[i]= int(l[i])
        i=i+1
l.sort()
print(l)

