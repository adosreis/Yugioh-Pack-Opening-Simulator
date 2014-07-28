
import json
import random
import os
set_objects = dict()

class decoded_set:
	rare = []
	commoners = []
	supers = []
	ultra = []
	ulti = []
	secret = []
	ghost = []


def sort_sets():
	sets = []
	for file in os.listdir('.'): #need to set this up
		if file.endswith('.json'):
			with open('./'+file) as json_data:
				sets_objects[str(file)]=decoded_set() #hoping this works so much!
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
	selected_pack_name = input(str("which pack? "+set_objects.keys()))
	selected_pack = set_objects[selected_pack_name]
	pack = []
	for i in range(7):
		pack.append(selected_pack.commoners[random.randint(0, (len(selected_pack.commoners)-1))])
	rarity = random.randint(0, 72)
	if rarity in range(0, 18):
		pack.append(selected_pack.supers[random.randint(0, (len(selected_pack.supers)-1))])
	if rarity in range(18, 24):
		pack.append(selected_pack.ultra[random.randint(0, (len(selected_pack.ultra)-1))])
	if rarity in range(24, 27):
		pack.append(selected_pack.ulti[random.randint(0, (len(selected_pack.ulti)-1))])
	if rarity in range(27, 31):
		pack.append(selected_pack.secret[random.randint(0, (len(selected_pack.secret)-1))])
	if rarity in range(31, 33):
		pack.append(selected_pack.ghost[random.randint(0, (len(selected_pack.ghost)-1))])
	if rarity in range(33, 73):
		pack.append(selected_pack.rare[random.randint(0, (len(selected_pack.rare)-1))])

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

