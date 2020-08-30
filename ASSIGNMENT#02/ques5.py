n=int(input("ENTER THE LIMIT OF LIST :"))
lst=[]
res=1
print("ENTER THE NUMBERS :")
for i in range(0,n):
    a=int(input())
    res*=a
    lst.append(a)
print("THE RESULT IS : ",res)