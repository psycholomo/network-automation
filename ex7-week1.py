#!/usr/bin/env python

#Write a python program that reads both yaml and the json file created in exercise6
# and pretty prints the data structure that is returned.

import yaml
import json
from pprint import pprint

def output_format(my_list, my_str):


	with open("ex6.yml") as openfile:
		pprint(yaml.load(openfile))

	with open("ex6.json") as openfile:
		json_data = json.load(openfile)
		pprint(json_data)

output_format("ex6.yml", ' YAML')
output_format("ex6.json", ' JSON')
print '\n'
		
