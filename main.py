
import json
import random
import os
set_objects = dict()

class decoded_set: #class to hold a specific sets cards
	rare = []
	commoners = []
	supers = []
	ultra = []
	ulti = []
	secret = []
	ghost = []


def sort_sets():
	for file in os.listdir('./jsons/'): 
		if file.endswith('.json'):
			with open('./jsons/'+file) as json_data:
				sets_objects[str(file)]=decoded_set()
				data = json.load(json_data)
				for x in data:
					if '\n' in x['rarity'] :
						for i in x['rarity'].split('\n'):
							if i == "Rare":
								set_objects[str(file)].rare.append(str(x['name']))
							if i == "Super Rare":
								set_objects[str(file)].supers.append(str(x['name']))
							if i == "Common":
								set_objects[str(file)].commoners.append(str(x['name']))			#if not totally fucked...
							if i == "Short Print":
								set_objects[str(file)].rare.append(str(x['name']))
							if i == "Ultra Rare":
								set_objects[str(file)].ultra.append(str(x['name']))
							if i == "Secret Rare":
								set_objects[str(file)].secret.append(str(x['name']))
							if i == "Ghost Rare":
								set_objects[str(file)].ghost.append(str(x['name']))
							if i == 'Ultimate Rare':
								set_objects[str(file)].ulti.append(str(x['name']))
					else:
						if x['rarity'] == "Rare":
							set_objects[str(file)].rare.append(str(x['name']))
						if x['rarity'] == "Super Rare":
							set_objects[str(file)].supers.append(str(x['name']))
						if x['rarity'] == "Common":
							set_objects[str(file)].commoners.append(str(x['name']))
						if x['rarity'] == "Short Print":
							set_objects[str(file)].rare.append(str(x['name']))
						if x['rarity'] == "Ultra Rare":
							set_objects[str(file)].ultra.append(str(x['name']))
						if x['rarity'] == "Secret Rare":
							set_objects[str(file)].secret.append(str(x['name']))
						if x['rarity'] == "Ghost Rare":
							set_objects[str(file)].ghost.append(str(x['name']))
						if x['rarity'] == 'Ultimate Rare':
							set_objects[str(file)].ulti.append(str(x['name']))
				
def generate_pack(): 
	selected_set_name = input(str("which pack? "+set_objects.keys()))
	selected_set = set_objects[selected_set_name]
	pack = []
	for i in range(7):
		pack.append(selected_set.commoners[random.randint(0, (len(selected_set.commoners)-1))])
	pack.append(selected_set.rare[random.randint(0, (len(selected_set.rare)-1))])
	rarity = random.randint(0, 359)
	if rarity in range(0, 72):
		pack.append(selected_set.supers[random.randint(0, (len(selected_set.supers)-1))])
	if rarity in range(72, 102):
		pack.append(selected_set.ultra[random.randint(0, (len(selected_set.ultra)-1))])
	if rarity in range(102, 117):
		pack.append(selected_set.ulti[random.randint(0, (len(selected_set.ulti)-1))])
	if rarity in range(117, 132):
		pack.append(selected_set.secret[random.randint(0, (len(selected_set.secret)-1))])
	if rarity in range(132, 147):
		pack.append(s elected_set.ghost[random.randint(0, (len(selected_set.ghost)-1))])
	if rarity in range(147, 360):
		pack.append(selected_set.commoners[random.randint(0, (len(selected_set.commoners)-1))])

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

