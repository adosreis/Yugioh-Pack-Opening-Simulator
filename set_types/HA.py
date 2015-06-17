#!/usr/bin/python3
import random

class Hidden_Arsenal_Like:
	#The sets that are considered Hidden Arsenal like:
	sets = ["HA01", "HA02", "HA03", "HA04", "HA05", "HA06", "HA07", "NUMH",
			"DRLG", "THSF"]

	#Create the empty arrays:
	def __init__(self):
		self.supers = []
		self.secret = []

	#Adds a card of the given name to the given rarity:
	def add_card(self, rarity, cardname):
		if(rarity == "Super Rare"):
			self.supers.append(cardname)
		if(rarity == "Secret Rare"):
			self.secret.append(cardname)

	#Shuffles all the rarities in one simple call:
	def shuffle(self):
		random.shuffle(self.supers)
		random.shuffle(self.secret)

	#Returns a pack of the set:
	def generate_pack(self):
		self.shuffle()
		pack = []
		for i in range(0, 4):
			pack.append(self.supers[i])
		pack.append(self.secret[0])
		return pack
