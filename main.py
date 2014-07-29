#!/usr/bin/python
import json
import random
import os
set_objects = dict()

class set: #class to hold a specific sets cards
	#Create the empty arrays:
	def __init__(self):
		self.commoners = []
		self.rare = []
		self.supers = []
		self.ultra = []
		self.ulti = []
		self.secret = []
		self.ghost = []

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

def sort_sets():
	for file in os.listdir('./jsons/'): 
		if file.endswith('.json'):
#			print file #for debugging the unicode 
			with open('./jsons/'+file) as json_data:
				set_name = os.path.splitext(str(file))[0]
				set_objects[set_name]=set()
				data = json.load(json_data)
				for x in data:
					if '\n' in x['rarity'] :
						for i in x['rarity'].split('\n'):
							set_objects[set_name].add_card(str(x['rarity']), str(x['name']))
					else:
						set_objects[set_name].add_card(str(x['rarity']), str(x['name']))

def generate_pack(): 
	print set_objects.keys()
	selected_set_name = input('which pack?')
	selected_set = set_objects[selected_set_name]
	pack = []
	selected_set.shuffle()
	for i in range (0, 7):
		pack.append(selected_set.commoners[i])
#	rarity = random.randint(0, 359)
#	if rarity in range(0, 72):
#		pack.append(selected_set.supers[random.randint(0, (len(selected_set.supers)-1))])
#	if rarity in range(72, 102):
#		pack.append(selected_set.ultra[random.randint(0, (len(selected_set.ultra)-1))])
#	if rarity in range(102, 117):
#		pack.append(selected_set.ulti[random.randint(0, (len(selected_set.ulti)-1))])
#	if rarity in range(117, 132):
#		pack.append(selected_set.secret[random.randint(0, (len(selected_set.secret)-1))])
#	if rarity in range(132, 147):
#		pack.append(selected_set.ghost[random.randint(0, (len(selected_set.ghost)-1))])
#	if rarity in range(147, 360):
#		pack.append(selected_set.commoners[random.randint(0, (len(selected_set.commoners)-1))])

	return pack
'''
print rare
print('----------------------------------------')
print commoners
print('----------------------------------------')
print supers
print('----------------------------------------')
print ultra
print('----------------------------------------')
print secret
print('----------------------------------------')
print ghost
print('----------------------------------------')
'''

def main():
	sort_sets()
	print generate_pack()

if __name__ == '__main__':
    main()
