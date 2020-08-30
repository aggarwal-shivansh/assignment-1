str=input("ENTER THE STRING :")
u,l=0,0
for i in range (0,len(str)):
    if(str[i].isupper()):
        u+=1
    else:
        l+=1
print("THE NUMBER OF UPPERCASE LETTERS IS :",u)
print("THE NUMBER OF LOWERCASE LETTERS IS :",l)