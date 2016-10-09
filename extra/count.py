import re
import operator

def user_count():
	word = input("Insert the word you want to count: ")
	local_count = 0
	global_count = 0
	with open("lyrics.txt", "r") as f:
  		for line in f:
			new_line = line
			#new_line = re.sub("[^a-zA-Z]+", " ", new_line) <- gets rid of all non-alphabet characters
			new_line = re.sub(",", "", new_line)
			line_array = new_line.split()
			for element in line_array:
				if word.lower() == element.lower():
					global_count+=1
	print(word +": " + str(global_count))

def count_all():
	while True:
		try:
			list_size = int(raw_input("Size of list: "))
			break
		except ValueError:
			print("Please input an integer. ")
	print(" ") #Used to create a blank line between actions in console
	word_count = {}
	with open("lyrics.txt", "r") as f:
  		for line in f:
			new_line = line
			new_line = re.sub(",", "", new_line)
			line_array = new_line.split()
			for element in line_array:
				check_word = element.lower()
				if check_word in word_count:
					word_count[check_word] +=1
				else:
					word_count[check_word] = 1
	#sorted(word_count.values())
	sorted_words = sorted(word_count.items(), key=operator.itemgetter(1))
	sorted_words.reverse()
	#word_count(sort_by_values=0, reversed=0)
	if list_size > len(sorted_words):
		list_size = len(sorted_words)
	for num in range(0,list_size):
		ranking = num+1
		print("#"+str(ranking) + ": " + '"{}"'.format(sorted_words[num][0]) + " found " +str(sorted_words[num][1]) + " times.")

if __name__ == "__main__":
	#user_count()
	count_all()
