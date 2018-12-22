#!/usr/bin/python3
#This script will change \x41\x42\x43 to 0x41,0x42,0x43
import os

shllcode = input("paste your shellcode \n> ")


new_shellcode = "0" + ",0".join(shllcode.split("\\")[1:])
os.system('clear')
print('\n')
print(new_shellcode)
