l=int(input("ENTER THE LIMIT :"))
tp=()
ls=[]
c=0
for i in range(2, l+1):
    c=0
    for j in range(1, i+1):
        if(i % j == 0):
            c += 1
    if c == 2:
        tp = i, 'PRIME'
        ls.append(tp)
    else:
        tp = i, 'NON PRIME'
        ls.append(tp)
print(ls)
input= "press enter to exit"