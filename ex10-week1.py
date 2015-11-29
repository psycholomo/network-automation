#!/usr/bin/env python

#Using ciscoconfparse find the crypto maps that are not using AES (Based on the #transform set name). Print these entries and their corresponding transform set name. 
import re
from ciscoconfparse import CiscoConfParse





cisco_cfg = CiscoConfParse('cisco_ipsec.txt')
cisco_crypto = cisco_cfg.find_objects_wo_child(parentspec=r'^crypto map CRYPTO', childspec=r'^AES')


for entry in cisco_crypto:
    print cisco_crypto
    for child in entry.children:
        if 'transform' in child.text:
            match = re.search(r"set transform-set (.*)$", child.text)
            encryption = match.group(1)

    print (entry.text.strip(), encryption)

