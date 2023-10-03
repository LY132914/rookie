name={}
name[1]='地平线'
name[2]='亡灵'
name[3]='电妹'
name[4]='屁男'
t={}
for i in name.keys():
    if(i%2) :
         t[i]=name[i]
name=t
for i in name.items() :
    print(i)