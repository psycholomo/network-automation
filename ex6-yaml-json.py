#!/usr/bin/env python
import yaml
import json


funny_dict = {'clowns' : 'cars',
             'elepahnts' : 'peanuts'




			 }


with open('ex6.yml', 'w') as outfile:
	outfile.write(yaml.dump(funny_dict, default_flow_style=True))

