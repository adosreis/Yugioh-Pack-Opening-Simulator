#all in all getting to this point after not programming for 2 months was pretty easy
import json
import random
data = []
pack = []
rare = []
commoners = []
supers = []
ultra = []
secret = []
ghost = []
with open('/Users/andrewdos2/Documents/yougiohthing/json_cards.json') as json_data:
	data = json.load(json_data)
	for x in data:
		print x['rarity']
		if x['rarity'] == "Rare":
			rare.append(x['name'])
		if x['rarity'] == "Super Rare":
			supers.append(x['name'])
		if x['rarity'] == "Common":
			commoners.append(x['name'])
		if x['rarity'] == "Short Print":
			rare.append(x['name'])
		if x['rarity'] == "Ultra Rare":
			ultra.append(x['name'])
		if x['rarity'] == "Secret Rare":
			secret.append(x['name'])
		if x['rarity'] == "Ulimate Rare":
			ultra.append(x['name'])
		if x['rarity'] == "Ghost Rare":
			ghost.append(x['name'])
for i in range(7):
	pack.append(commoners[random.randint(0, (len(commoners)-1))])
print pack

#this is all commented out because i was trying to show parsing
#they all work excpet ultra and ghost because of the multi-rarities
#thats why we have to simplify
#you can uncomment if you want to see them in action
'''print rare
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

