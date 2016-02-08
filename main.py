#!/usr/bin/python3
import json
import random
import os
from set_types import *
set_objects = dict()

def sort_sets():
	for file in os.listdir(os.path.join('.', 'jsons')): 
		if file.endswith('.json'):
			with open(os.path.join('jsons', file)) as json_data:
				#Get the set name:
				set_name = os.path.splitext(str(file))[0]

				#Identify what kind of set this is:
				for i in CS.Core_Set.sets:
					if(set_name.startswith(i)):
						set_objects[set_name] = CS.Core_Set()

				for i in HA.Hidden_Arsenal_Like.sets:
					if(set_name.startswith(i)):
						set_objects[set_name] = HA.Hidden_Arsenal_Like()

				for i in GS.Gold_Series.sets:
					if(set_name.startswith(i)):
						set_objects[set_name] = GS.Gold_Series()

				for i in BP.Battle_Pack.sets:
					if(set_name.startswith(i)):
						set_objects[set_name] = BP.Battle_Pack()

				data = json.load(json_data)
				for x in data:
					if '\n' in x['rarity'] :
						for i in x['rarity'].split('\n'):
							set_objects[set_name].add_card(str(i), str(x['name']))
					else:
						set_objects[set_name].add_card(str(x['rarity']), str(x['name']))



def main():
	sort_sets()

	print(set_objects.keys())
	selected_set_name = input('which pack?')
	selected_set = set_objects[selected_set_name]

	print(selected_set.generate_pack())

if __name__ == '__main__':
    main()
