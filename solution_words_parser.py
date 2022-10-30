import os,sys

solution_file = open("solution_words.txt","r")
content = solution_file.read()
content = content.split("\n")
final_list= []
for i in content:
	final_list.append(i[-5:].lower())
print(final_list)

new_file = open("all_solution_words.txt","w")
new_file.write(','.join(final_list))
new_file.close()