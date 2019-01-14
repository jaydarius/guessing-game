"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    # store and load functions adapted from https://stackoverflow.com/a/53684733/10221777
    def store_highscore_in_file(dictionary, fn = "./highscore.txt"):
        """Store the dict into a file, only store top_n highest values."""
        with open(fn,"w") as f:
            for name, guesses in dictionary.items():
                f.write(f"{name}:{guesses}\n")
                

    def load_highscore_from_file(fn = "./highscore.txt"):
        """Retrieve dict from file"""
        hs = {}
        try:
            with open(fn,"r") as f:
                for line in f:
                    name,_,guesses = line.partition(":")
                    if name and guesses:
                        hs[name]=int(guesses)
        except FileNotFoundError:
            return {}
        return hs

    banner = "="*30
    guessing = True
    chosen_num = random.randint(1,20)
    count = 1
    highscore = load_highscore_from_file()

    print("{}\nWelcome to the Python guessing game!\n{}\n".format(banner, banner))
    if highscore:
        print("The high score is {} tries.\n".format(highscore["player"]))
    

    while guessing:
        
        guess = input("Pick a number between 1 and 20: ")

        try:
            guess = int(guess)    
        except ValueError:
            print("Numbers only please!\n")
            continue

        if (guess <= 0) or (guess > 20):
            print("Number is not between one and 20!\n")
            continue
        if guess < chosen_num:
            print("Guess higher!\n")
        elif guess > chosen_num:
            print("Guess lower!\n")
        else:
            print("**Correct**!\nIt took you {} tries!\n".format(count))
            if count < highscore["player"]:
                store_highscore_in_file({"player": count})
            guessing = False
        
        count += 1
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            start_game()
        else:
            print("\nThanks for playing! Exiting the game now :)")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
