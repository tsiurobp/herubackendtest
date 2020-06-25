#Author: Tonantzin Siurob
#Date: June 2020
#Contact: tonasiurob@gmail.com

import sys
import codecs

def read_vocabulary(file_name):
	#contains all the words to work with
	vocabulary_list = list()
	f = codecs.open(file_in, "r", "utf-8")
	for line in f:
		line = line.strip()
		line_words = line.split()
		for each in line_words:
			vocabulary_list.append(each)
	return vocabulary_list

def order_vocabulary(word_list, alphabet):
	ordered_list = list()
	ordered_list = sorted(word_list, key=lambda word: [alphabet.index(c) for c in word])
	return ordered_list

def create_vocabulary_string(vocabulary_list):
	output_string = ''
	for each in vocabulary_list:
		output_string = output_string + each + ' '
	return output_string

def count_prepositions(vocabulary_list):
	count = 0
	foo_letters = 'udxsmpf'
	for each in vocabulary_list:
		if len(each) == 6:
			if 'u' not in each:
				last_letter = each[-1]
				if last_letter in foo_letters:
					#print(each)
					count += 1
	return count

def count_verbs(vocabulary_list):
	count_verbs = 0
	count_verbs_subjunctive = 0
	foo_letters = 'udxsmpf'
	for each in vocabulary_list:
		if len(each) >= 6:
			last_letter = each[-1]
			if last_letter not in foo_letters:
				#print(each)
				count_verbs +=1
				start_letter = each[0]
				if start_letter not in foo_letters:
					#print(each)
					count_verbs_subjunctive += 1
	return count_verbs, count_verbs_subjunctive

def create_number_list(vocabulary_list, alphabet):
	number_list = list()
	for each in vocabulary_list:
		aux = 0
		number = 0
		total = 0
		for c in each:
			#print(c)
			number = (alphabet.index(c))*(20**aux)
			total = total + number
			aux += 1
		number_list.append(total)
	return number_list

def count_pretty_numbers(number_list):
	pretty_numbers_dict = dict()
	numbers_count = 0
	for each in number_list:
		if each >= 81827:
			if (each % 3) == 0:
				#print(each)
				pretty_numbers_dict[each] = 1
	#print(pretty_numbers_dict)
	numbers_count = len(pretty_numbers_dict)
	return numbers_count


	


if __name__ == "__main__":
	alphabet = 'sxocqnmwpfyheljrdgui'
	initial_vocabulary = list()
	ordered_vocabulary = list()
	number_list = list()
	output_vocabulary = ''
	preposition_frequency = 0
	verb_frequency = 0
	subjunctive_verb_frequency = 0
	pretty_numbers_frequency = 0

	file_in = sys.argv[1] #initial string file name
	initial_vocabulary = read_vocabulary(file_in)
	ordered_vocabulary = order_vocabulary(initial_vocabulary, alphabet)
	output_vocabulary = create_vocabulary_string(ordered_vocabulary)

	preposition_frequency = count_prepositions(ordered_vocabulary)

	(verb_frequency, subjunctive_verb_frequency) = count_verbs(ordered_vocabulary)

	number_list = create_number_list(ordered_vocabulary, alphabet)
	pretty_numbers_frequency = count_pretty_numbers(number_list)

	print('1) There are {} prepositions in the text'.format(preposition_frequency))
	print('2) There are {} verbs in the text'.format(verb_frequency))
	print('3) There are {} subjunctive verbs in the text'.format(subjunctive_verb_frequency))
	print('4) Vocabulary list:')
	print('\t{}'.format(output_vocabulary))
	print('5) There are {} distinct pretty numbers in the text'.format(pretty_numbers_frequency))


	