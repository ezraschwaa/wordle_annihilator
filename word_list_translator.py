#Converts word file from a string to txt file list
import sys

filename = "wordle-list/words"
my_file=open(filename,"r")
#Break into BST?
content = my_file.read()
new_file = open("words_text.txt","w")
new_file.write(content)
new_file.close()
