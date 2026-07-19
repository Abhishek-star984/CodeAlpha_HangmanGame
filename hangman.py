import random

# Predefined list of words
words = ["python", "apple", "banana", "computer", "school"]

# Choose a random word
word = random.choice(words)

# Create hidden word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)