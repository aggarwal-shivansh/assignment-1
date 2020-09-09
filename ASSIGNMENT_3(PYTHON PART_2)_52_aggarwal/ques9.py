def count_primes(n):
    c,t = 0,0
    for i in range(2,n+1):
        c = 0
        for j in range(1,i+1):
            if i%j == 0:
                c+=1
        if(c == 2):
            t+=1
    return t
n = int(input("ENTER THE NUMBER : "))
print(count_primes(n))