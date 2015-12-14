#!/usr/bin/env python
###
#Write a script that connects to the lab pynet-trt1, logins, and exectures the
# 'show ip int brif'command.
###


import telnetlib
import time
import socket
import sys
import getpass


def send_command(remote_conn, cmd):
	telnet_port = 23
	telnet_timeout = 6
	cmd = cmd.rstrip()
	remote_conn.write(cmd + '\n')
	time.sleep(1)
	return remote_conn.read_very_eager()

def 
