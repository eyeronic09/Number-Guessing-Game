import random 

computerNumber = random.randint(1,3)
print(computerNumber)
while True:
    userNumber = int(input("enter the number"))
    if computerNumber == userNumber:
        print(f"congratulations you  guessed the  ")
        break
    elif userNumber >= computerNumber:
        print(f"the gusse is to high ")
    elif userNumber <= computerNumber:
        print(f"the gusse is to low ")