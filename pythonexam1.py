print("=" * 40)
print("WELCOME TO THE NUMBER GUESS GAME")
print("=" * 40)
print("In this game, you will try to guess a secret number between 1 and 50.")
sec_num = 13
guess = 0
while sec_num != guess:
    guess = int(input("Enter your guess: "))
    if guess == 1:
        print("your number is hot 🌡️")
    elif guess > 10 and guess < 20:
        print("your number is is very hot 🔥")
    elif guess > 20 and guess < 30:
        print("your number is warm 🌞")
    elif guess > 30 and guess < 40:
        print("your number is cold ❄️")
    elif guess > 40 and guess < 50:
        print("your number is ice cold 🥶")
        for i in range(1, 4):
    else:
        print("Congratulations! You guessed the secret number!")

