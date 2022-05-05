from random import random

from matplotlib.pyplot import draw
from numpy import empty
from draw_hangman import drawings
import english_words

class HangmanGame():
	def __init__(self):
		self.words = list(english_words.english_words_lower_alpha_set)
		self.length = len(self.words)
		self.drawings = drawings
		self.max_attempts = max(self.drawings.keys())
		self.attempt = 0
		self.guesses = []
	
	def get_random_word(self):
		index = int(random()*self.length)
		return self.words[index]
	
	def check_letter_or_word(self, guess):
		if guess in self.guesses:
			return {'result': 'next', 'message': "\nSorry, you already guessed that one. Try something else.\n".format(guess)}
		
		self.guesses.append(guess)
		
		if len(guess) > 1:
			if guess == self.word:
				self.empty_word = guess
				return {'result': 'done', 'message': "\nCongratulations, {} is the word!\n".format(guess)}
			else:
				self.attempt += 1
				return {'result': 'next', 'message': "\nSorry, {} is not the word!\n".format(guess)}
		else:
			if guess in self.word:
				for i in range(len(self.word)):
					if self.word[i] == guess:
						self.empty_word = list(self.empty_word)
						self.empty_word[i] = guess
						self.empty_word = ''.join(self.empty_word)
				return {'result': 'next', 'message': "\nGood job, {} is in the word!\n".format(guess)}
			else:
				self.attempt += 1
				return {'result': 'next', 'message': "\nSorry, {} is not in the word!\n".format(guess)}

	def get_game_situation(self):
		if self.attempt == self.max_attempts:
			return 'Game over, {} was the word.'.format(self.word)
		elif self.empty_word == self.word:
			return "\nCongratulations, {} is the word!".format(self.word)
	
	def initialize_game(self):
		self.word = self.get_random_word()
		self.attempt = 0
		self.guesses = []
		self.empty_word = '_' * len(self.word)
		
		print("Let's play Hangman!")
		print(self.drawings[self.attempt])

		print('\nGuesses: {}'.format(self.guesses))
		print("\n{} letters: ".format(len(self.word))+self.empty_word)
		

	
	def next_round(self):
		situation = self.get_game_situation()
		if situation != None:
			print(situation)
		else:
			print(self.drawings[self.attempt])

			print('\nYou can fail {} more time(s).'.format(self.max_attempts-self.attempt))
			print('\nGuesses: {}'.format(self.guesses))
			print("\n{} letters: ".format(len(self.word))+self.empty_word)
			self.play()

	
	def play(self):
		if self.attempt == 0 and len(self.guesses) == 0:
			self.initialize_game()
		
		print('\n'+'*'*75)
		guess = input('\nPlease guess a letter or word: ')
		result = self.check_letter_or_word(guess)
		if (result['result'] == 'done'):
			print(result['message'])
		else:
			print(result['message'])
			self.next_round()

		

hangman = HangmanGame()
hangman.play()