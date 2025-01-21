#!/usr/bin/env python3
'''Testing os.system() commands'''
import os

# Run Linux commands
os.system('ls')
os.system('whoami')
os.system('ifconfig')

# Capture and print return values
ls_return = os.system('ls')
print('The contents of ls_return:', ls_return)

whoami_return = os.system('whoami')
print('The contents of whoami_return:', whoami_return)

ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:', ifconfig_return)

ipconfig_return = os.system('ipconfig')  # Command will fail
print('The contents of ipconfig_return:', ipconfig_return)

