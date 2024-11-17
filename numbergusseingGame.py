import random

def printmenu():
    print('''
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    ''')

printmenu()
computerNumber = random.randint(1,100)

while True:
    difficulty = int(input("Enter your choice (1 = Easy, 2 = Medium, 3 = Hard): "))
    if difficulty not in [1, 2, 3]:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue
        
    if difficulty == 1:
        max_attempts = 10
    elif difficulty == 2:
        max_attempts = 5
    elif difficulty == 3:
        max_attempts = 3
        
    attempts = 0
    
    while attempts < max_attempts:
        print(f"\nAttempt {attempts + 1}/{max_attempts}")
        userNumber = int(input("Enter your guess (1-100): "))
        attempts += 1
        
        if computerNumber == userNumber:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            exit()
        elif userNumber > computerNumber:
            print("The guess is too high")
        else:
            print("The guess is too low")
            
        if attempts >= max_attempts:
            print(f"\nGame Over! You've used all your {max_attempts} attempts.")
            print(f"The number was {computerNumber}")
            exit()