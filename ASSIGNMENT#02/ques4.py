n=int(input("ENTER THE LIMIT OF LIST :"))
lst=[]
arr=[]
print("ENTER THE NUMBERS :")
for i in range(0,n):
    a=int(input())
    lst.append(a)
for i in lst:
    if i not in arr:
        arr.append(i)
print(arr)
