import random

# Generate the target number ONCE outside the loop
target_number = random.randint(1, 20)
attempts_allowed = 5
counter = 1

print("--- Welcome to the Guessing Game! ---")

while counter <= attempts_allowed:
    guess = int(input(f"Attempt {counter}/{attempts_allowed}: Guess a number (1-20): "))
    
    if guess == target_number:
        print(f"🎉 Correct! You guessed {target_number} in {counter} attempts.")
        break
    else:
       
        if guess < target_number:
            print("Too low!")
        else:
            print("Too high!")
        
        counter += 1
else:
    
    print(f"\nGame Over! You're out of attempts. The number was {target_number}.")