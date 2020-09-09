def summer_69(arr):
    s= 0
    f = True
    for num in arr:
        while f:
            if num != 6:
                s += num
                break
            else:
                f = False
        while not f: 
            if num != 9:
                break
            else: 
                f = True
                break
    return s
arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print("THE SUM IS : ",summer_69(arr))

