#!/usr/bin/python3
import random

class Battle_Pack:
	#The Battle Packs - excluding BP01, see
	#<https://github.com/adosreis/Yugioh-Pack-Opening-Simulator/wiki/Battle-Pack-1>:
	sets = ["BP02", "BP03"]

	#Create the empty arrays:
	def __init__(self):
		self.commons = []
		self.rares = []
		self.shiny = []

	#Adds a card of the given name to the given rarity:
	def add_card(self, rarity, cardname):
		if(rarity == "Common"):
			self.commons.append(cardname)
		if(rarity == "Rare"):
			self.rares.append(cardname)
		if((rarity == "Mosaic Rare") or (rarity == "Shatterfoil")):
			self.shiny.append(cardname)

	#Shuffles all the rarities in one simple call:
	def shuffle(self):
		random.shuffle(self.commons)
		random.shuffle(self.rares)
		random.shuffle(self.shiny)

	#Returns a pack of the set:
	def generate_pack(self):
		self.shuffle()
		pack = []
		pack.append(self.rares[0])
		for i in range(0, 3):
			pack.append(self.commons[i])
		pack.append(self.shiny[0])
		return pack
