#!/usr/bin/python3
#This script will change \x41\x42\x43 to 0x41,0x42,0x43

shllcode = input("Your shellcode file location (.txt) (/root/...): \n> ")

# Edit this line with the path to the binary file containing shellcode you are converting
with open(shllcode, 'r+') as sc_handle:
	sc_data = sc_handle.read()

new_shellcode = "0" + ",0".join(sc_data.split("\\")[1:])
print(cs_shellcode)




