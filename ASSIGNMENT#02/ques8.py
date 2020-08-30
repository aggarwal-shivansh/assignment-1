l=int(input("ENTER THE LIMIT :"))
d={}
ls=[]
c,f=0,0
for i in range(2, l+1):
    c=0
    for j in range(1, i+1):
        if(i % j == 0):
            c += 1
    if c == 2:
        d[i] = "PRIME"
    else:
        d[i] = "NON PRIME"
        f += 1
print(d)
for i,val in d.items():
        if val == "NON PRIME" :
            ls.append(i)
for i in ls:
    del d[i]
print("AFTER DELETION THE RESULTANT DICTIONARY IS :")
print(d)
print("NUMBER OF ELEMENTS DELETED IS :",f)