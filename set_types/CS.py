#!/usr/bin/python3
import random

class Core_Set:
	#The sets considered to be core sets (this isn't correct at all, and we
	#will need to break these down further because ratios and things change
	#over time, but it'll do us for now:
	sets = ["LOB", "MRD", "SRL", "PSV", "LON", "LOD", "PGD", "MFC", "DCR",
			"IOC", "AST", "SOD", "RDS", "FET", "TLM", "CRV", "EEN", "SOI",
			"EOJ", "POTD", "CDIP", "STON", "FOTB", "TAEV", "GLAS", "PTDN",
			"LODT", "TDGS", "CSOC", "CRMS", "RGBT", "ANPR", "SOVR", "ABPF",
			"TSHD", "DREV", "STBL", "STOR", "EXVC", "GENF", "PHSW", "ORCS",
			"GAOV", "REDU", "ABYR", "CBLZ", "LTGY", "JOTL", "SHSP", "LVAL",
			"PRIO", "DUEA", "NECH", "SECE", "CROS", "CORE", "DOCS" ] 

	#Create the empty arrays:
	def __init__(self):
		self.commoners = []
		self.rare = []
		self.supers = []
		self.ultra = []
		self.ulti = []
		self.secret = []
		self.ghost = []

	#Adds a card of the given name to the given rarity:
	def add_card(self, rarity, cardname):
		if(rarity == "Common"):
			self.commoners.append(cardname)
		if(rarity == "Rare"):
			self.rare.append(cardname)
		if(rarity == "Super Rare"):
			self.supers.append(cardname)
		if(rarity == "Ultra Rare"):
			self.ultra.append(cardname)
		if(rarity == "Ultimate Rare"):
			self.ulti.append(cardname)
		if(rarity == "Secret Rare"):
			self.secret.append(cardname)
		if(rarity == "Ghost Rare"):
			self.ghost.append(cardname)

	#Shuffles all the rarities in one simple call:
	def shuffle(self):
		random.shuffle(self.commoners)
		random.shuffle(self.rare)
		random.shuffle(self.supers)
		random.shuffle(self.ultra)
		random.shuffle(self.ulti)
		random.shuffle(self.secret)
		random.shuffle(self.ghost)

	#Returns a pack of the set:
	def generate_pack(self): 
		self.shuffle()
		pack = []
		pack.append(self.rare[0])
		for i in range (0, 7):
			pack.append(self.commoners[i])
		rarity = random.randint(0, 359)
		if rarity in range(0, 72):
			pack.append(self.supers[0])
		if rarity in range(72, 102):
			pack.append(self.ultra[0])
		if rarity in range(102, 117):
			pack.append(self.ulti[0])
		if rarity in range(117, 132):
			pack.append(self.secret[0])
		if rarity in range(132, 147):
			pack.append(self.ghost[0])
		if rarity in range(147, 360):
			pack.append(self.commoners[7])
		return pack
