# wordle_annihilator
Solves world in a max of 4 guesses

To run, download repo and run `world_guesser.py`.  

Todo, add a best guess insight-er using probablilities.  

1st step, put in all guessed letters. this removes any word from the master list that has that letter.

2nd step, add yellow letters in the form of five underscores (no spaces) "_____". (E.g., _e_a_) currently only supports one yellow letter per place. this removes any word with that letter in that position 

3rd step, enter green letters. 

Then, shows all possible words. Some words may be missing because this uses a "wordle masterlist".  in the future it might be better to create a unique library of brute forced 5 letter words and seeing if they are in the dictionary.
