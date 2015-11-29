#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
cisco_pfs = cisco_cfg.find_objects_w_child(parentspec=r'^crypto map CRYPTO', childspec=r'pfs group2')

for i in cisco_pfs:
 print i.text 
