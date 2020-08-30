str=input("ENTER THE STRING TO CHECK : ")
l=len(str)
f=0
for i in range(0,l):
    if(str[i]!=str[l-i-1]):
        f=1
        break
if(f==0):
    print("PALLINDROME ")
else:
    print("NOT PALLINDROME ")