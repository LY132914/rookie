input_list=eval(input())
l=[]
for i in input_list:
    if(type(i)==int):
        l.append(i);
l.sort()
print(l)

