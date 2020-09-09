def spy_game(nums):
    count=0
    for i in nums:
        if(i==0 and count==0):
            count=1
        if(i==0 and count==1):
            count=2
        if(i==7 and count ==2):
            count =3
    return count
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
if spy_game(lst) == 3:
    print("True")
else:
    print("False")