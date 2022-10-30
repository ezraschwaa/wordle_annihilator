#Code by Ezra
#This code is meant to perform 'data science' on wordle solutions
#In order to find a better heuristic for guessing
import os,sys
from collections import Counter

ALPHABET_KELVIN_VALUE = 97
MAX_LENGTH_WORD	= 5
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_LIST = list(ALPHABET)

filename = "all_solution_words.txt"
solutions_words = open(filename,"r")
solutions_words = solutions_words.read().split(',')
NUM_SOLUTIONS = len(solutions_words)


def most_common_letter_at_index(master_list, index):
	alphabet_count = [0]*26
	for word in master_list:
		letter_index = ord(word[index])-ALPHABET_KELVIN_VALUE
		alphabet_count[letter_index]+=1
	return alphabet_count

def parse_data(master_list, index):
	#Recieves all 26 letters by quantity
	new_list = {}
	data = most_common_letter_at_index(master_list,index)
	for i in range(len(data)):
		new_list[ALPHABET_LIST[i]] = data[i]
	return new_list

def give_sorted_dict(dictionary):
	#Returns a sorted dictionary
	return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse = True))

def give_top_5(dictionary):
	#Given a dictionary of string:integer K:v pairs returns top five v's and their key
	#All solutions from: https://stackoverflow.com/questions/7197315/5-maximum-values-in-a-python-dictionary
	#return (sorted(dictionary, key=dictionary.get, reverse=True)[:5])
	#return (max(dictionary.items(), key = lambda k : k[:1]))
	return dict(Counter(dictionary).most_common(5))

def give_top_words(master_list, amount_requested = 5):
	#give a heuristic for next statistcally best next word
	#does not include giving new unique letters (yet)
	data = [] #This will be a list of 5 sorted dictionaries.
	return None

def give_list_of_top_letters_at_index(master_list,i):
	#This will do what the first part of give_report does.
	return None

#Return this at the end of wordle guesser for in depth analysis!
def give_report(words_list):
	for i in range(MAX_LENGTH_WORD):
		data = parse_data(words_list,i)
		sorted_data = give_sorted_dict(data)
		top_5_items = give_top_5(sorted_data)
		print("Index "+str(i)+": "+str(top_5_items))
		#print(sorted_data)
		#print(top_5_items)

#__main__
give_report(solutions_words)

