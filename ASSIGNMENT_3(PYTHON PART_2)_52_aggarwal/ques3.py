def reversed_words(str):
    splitted = str.split()
    l = len(splitted)
    for i in range (0,l//2):
        t = splitted[i]
        splitted[i] = splitted[l-i-1]
        splitted[l-i-1] = t
    st = ' '.join(splitted)
    return st
str = input("ENTER THE STRING TO REVERSE : ")
st = reversed_words(str)
print(st)