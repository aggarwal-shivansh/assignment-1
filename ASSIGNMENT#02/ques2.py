lr=int(input("ENTER THE LOWER LIMIT :"))
ur=int(input("ENTER THE UPPER LIMIT :"))
num=int(input("ENTER THE NUMBER TO CHECK :"))
if num in range(lr,ur+1):
    print("NUMBER EXIST IN RANGE ")
else:
    print("NUMBER DO NOT EXIST ")
