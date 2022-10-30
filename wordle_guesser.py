#Given a word in the format _ _ _ _ _ the program will return all possible
#words that fit in the alphabet scheme given.  program will also allow
#to exlclude tried words
import sys, os
import analyzer_solutions as ass

#Open local files
words_file = "words_text.txt"
solution_words_file = "all_solution_words.txt"
words_open_file=open(words_file,"r")
solution_words_open_file = open(solution_words_file,"r")
content = words_open_file.read()
solution_content = solution_words_open_file.read()
total_five_letter_word_list = content.split('\n')
solutions = solution_content.split(',')

#Better way to do this--create list then weed, or brute force all? BST? Data structure? Radix?
final_list = []

#Try building a library that creates a box
print('#'*40)
print("")
print(' '*12 + "WORDLE GUESSER\n")
print('#'*40)

#Takes Input
tried_letters = list(input("\n1. Enter any attempted letters to exclude: \n>"))
possible_letters = list(input("\n2. Enter any yellow letters\nIn the format _ _ _ _ _\n>>"))
correct_format = False
while(not correct_format):
	word = input("\n3. Enter your word you'd like to solve\nIn the format _ _ _ _ _\n>>>")
	if len(word) != 5:
		continue
	else:
		correct_format = True

#returns how many yellow letters must be contained in a word
def yellow_letters_count(possibles):
	yellow_letters = 0
	for i in possibles:
		if(i!='_'):
			yellow_letters +=1
		else:
			continue
	return yellow_letters

def eliminate_words(master_list, solutions_list, bad_letters, past_guess):
#Solves for best words to use
	temp_list,solutions_temp_list = [],[]
	#Run through each letter in our solver
	for letter in range(len(word)):
		#First we check if the space is empty
		if(word[letter] == '_'):
			for item in master_list:
				#If we haven't tried the letter its a possibility
				#The && condition checks that if we know a letter doesn't belong there we can exclude it
				#!!!!! need to expand this line so that second condition check can include multiple lines!
				if(item[letter] not in bad_letters and item[letter] != past_guess[letter]):
					temp_list.append(item)
					if(item in solutions_list):
						solutions_temp_list.append(item)
		#If we have no reason to exclude, we check if we know a letter
		#If we have a letter, we include it for the next round
		else:
			for item in master_list:
				if(item[letter] == word[letter]):
					#A letter matches!
					temp_list.append(item)
					if(item in solutions_list):
						solutions_temp_list.append(item)

		master_list = temp_list
		solutions_list = solutions_temp_list

		solutions_temp_list = []
		temp_list = []
	return solutions_list,master_list

good_guesses,all_possible_words = eliminate_words(total_five_letter_word_list,solutions,tried_letters,possible_letters)
print(len(good_guesses))

#Now we need to remove all words that don't contain a yellow letter
def contains_yellows_check(possibles, word_list):
	end_words = []
	temp_count = 0
	yellow_count = yellow_letters_count(possibles)
	for item in word_list:
		temp_count = 0
		for i in range(len(item)):
			for letter in possibles:
				if(letter == '_'):
					continue
				elif(letter == item[i]):
				#This creates a bug! in the case of repeating letters.
					temp_count+=1
		if(temp_count>=yellow_count):
			end_words.append(item)
	return end_words

good_guesses = contains_yellows_check(possible_letters, good_guesses)

# print("Final List("+str(len(all_possible_words))+"): ")
# print(all_possible_words)

ass.give_report(good_guesses)
print("\nSolutions List("+str(len(good_guesses))+"): ")
print(good_guesses)


new_yellows = list(input("\nAre there other attempts with yellows to exclude?\nEnter in format _ _ _ _ _ \n>>"))
good_guesses, _ = eliminate_words(all_possible_words,good_guesses, tried_letters, new_yellows)
good_guesses = contains_yellows_check(new_yellows,good_guesses)
print(good_guesses)
