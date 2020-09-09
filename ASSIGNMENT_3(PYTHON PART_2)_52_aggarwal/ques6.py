def blackjack(a,b,c):
    sum = a+b+c
    if sum < 21 :
        return sum
    elif (sum > 21 and (a == 11 or b == 11 or c == 11)) :
        return (sum-10)
    else:
        return 'BUST'
a = int(input("ENTER FIRST NUMBER : "))
b = int(input("ENTER SECOND NUMBER : "))
c = int(input("ENTER THIRD NUMBER : "))
print(blackjack(a,b,c))