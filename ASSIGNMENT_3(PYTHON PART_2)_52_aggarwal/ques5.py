def has_33(lst):
    for i in range (0,n):
        if lst[i] == 3 and lst[i+1] ==3  :
            return True
    return False
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print(has_33(lst))
