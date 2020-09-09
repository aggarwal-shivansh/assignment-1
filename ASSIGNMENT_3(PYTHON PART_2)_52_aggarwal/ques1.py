import string
def check(str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in alpha:
        if ch not in str.upper():
            return False
    return True
string=input("ENTER THE STRING TO CHECK : ")
if(check (string) == True):
    print("YES")
else:
    print("NO")