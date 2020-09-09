def no_check(a,b):
    if(a%2 == 0 and b%2 == 0):
        return a if a < b else b 
    else:
        return a if a > b else b 
x = int(input("ENTER THE FIRST NUMBER : "))
y = int(input("ENTER THE SECOND NUMBER : "))
res = no_check(x,y)
print(res)

