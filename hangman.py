import random
words = ["Internship", "LetterOfRecommendation", "Placement", "PythonSkills", "ArtificialIntelligence"]
max_attempt = 6
sec_word = random.choice(words).lower()
guessed_letters = []
wrong_guess = 0

print("\n\nX-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
print("WELCOME TO THE HANGMAN GAME!!!!!!!")
print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X\n\n")

while wrong_guess < max_attempt:
    print_word = ""
    for ch in sec_word:
        if ch in guessed_letters:
            print_word += ch + " "
        else:
            print_word += "_ "
    print(print_word)
    guess = input("Guess a letter : ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter:",guess,"Try a different one.\n")
        continue
    guessed_letters.append(guess)
    if guess not in sec_word:
        wrong_guess+=1
        print("Letter",guess,"is not in the word!!!")
        print("Attempts Left = ",max_attempt - wrong_guess)
        print("\n")
    else:
        print("Very Good!",guess,"is in the word\n")
    won = True
    for ch in sec_word:
        if ch not in guessed_letters:
            won = False
    if won:
        print("CONGRATS!!!!! YOU WON THE GAME.")
        print(sec_word.title(),"was the word")
        break
    if wrong_guess == max_attempt:
        print("GAME OVER!!!")
        print("The word was : ", sec_word)