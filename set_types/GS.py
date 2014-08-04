#!/usr/bin/python3
import random

class Gold_Series:
	#The sets that are considered Hidden Arsenal like:
	sets = ["GLD1", "GLD2", "GLD3", "GLD4"]

	#Create the empty arrays:
	def __init__(self):
		self.commons = []
		self.golds = []

	#Adds a card of the given name to the given rarity:
	def add_card(self, rarity, cardname):
		if(rarity == "Common"):
			self.commons.append(cardname)
		if(rarity == "Gold Rare"):
			self.golds.append(cardname)

	#Shuffles all the rarities in one simple call:
	def shuffle(self):
		random.shuffle(self.commons)
		random.shuffle(self.golds)

	#Returns a pack of the set:
	def generate_pack(self):
		self.shuffle()
		pack = []
		for i in range(0, 3):
			pack.append(self.golds[i])
		for i in range(0, 22):
			pack.append(self.commons[i])
		return pack
