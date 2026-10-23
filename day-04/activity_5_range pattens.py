secret_number = 12
attempt = 0
guessed_correctly= False
while attempt < 5 and guessed_correctly==False:
    guess =input("Guess an number")
    if guess.isdigit()==False:
        guess.val= int(guess)
        if guess.value <0 and guess.val > 20:
            print("the correct value is 1 to 20")
        else:
            attempt += 1
            if guess.val==secret_number:
                print("YES, CORRECT")
                guessed_correctly = True
            elif guess_val < secret_number:
                print("TOO LOW")
            else:
                print("TOO HIGH")
if guessed_correctly == False:
    print(f"Failed to guess.Secret number is {secret_number}")