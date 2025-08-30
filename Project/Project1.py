import random
def guess_number():
    
    print("Let's guess the number")
    while True:
        # Chọn độ khó cho game
        print("\nChoose difficulty: ")
        print("1. Easy (1-50) within 10 turns ")
        print("2. Medium (1-75) within 9 turns")
        print("3. Hard (1-100) within 5 turns")
        mode = input("Enter 1,2 or 3 to choose the difficulty: ")
        if mode == '1':
            max_attempt = 10
            max_secret = 50
        elif mode == '2':
            max_attempt = 9
            max_secret = 75
        elif mode == '3':
            max_attempt = 5
            max_secret = 100
        else: 
            print("Invalid choice")
            continue
        secret = random.randint(1,max_secret)
        attempt = 0
        while attempt <= max_attempt:
            try:
                guess = int(input(f"\nGuess a number from 1 to {max_secret}: ,you have {max_attempt} turns: "))
            except ValueError:
                print("Invalid choice !!!")
                continue
            attempt +=1
            if guess < secret:
                print("Too low")
            elif guess > secret:
                print("Too high")
            else:
                print(f"Correct!! you guessed the right number after {attempt} turns")
                break 
        else:
            print("Game over!")
            print(f"The secret number is {secret}")
        again = input("\nWanna play again? (y/n): ").lower()
        if again != 'y':
            print("Thankyou for playing! See you next time")
            break


guess_number()