import random
words = ["soap", "car", "key", "house", "grandma", "jewsh", "mouse", "india", "shower"]
word = random.choice(words)
guessed = ['-'] * len(word)  
print("the word is :", ''.join(guessed))
score = 0
while True:
    
    human_guess = input("enter your guess: ").lower()
    
    if human_guess in word:
        print("wow good job!")
        for i in range(len(word)):
            if word[i] == human_guess:
                guessed[i] = human_guess 
        print("the word is:", ''.join(guessed))
    else:
        print("try again!")
        score += 1
    if score == 5:
        print("you used 5 try")
        print("Game Lose")
        print("-------------------------------------------------")
        break
        
    if "-" not in guessed:
        print("victory")
        print("game end")
        print("-------------------------------------------------")
        break
#بازي هنگ من يا همان حدس کلمات