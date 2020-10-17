def GetXORValue(xorv, name):
	nonflip = ''
	for c in name[i:i+4]
		nonflip += str(hex(ord(c))[2:])[::-1]
	xorv = nonflip[::-1]
	return xorv

encryption_buffer = 0x4e6af4bc
username = input("Enter Username: ")
full_key = "FIT-"
min_username_len = 5
username_len = len(username)

while(username_len < min_username_len):
	username = input(f"Enter username greater than {min_username_len}")
	username_len = len(username)

i=0
nonflippedvalue = ''
xor_value = GetXORValue('', username)
username_len -= 4
encryption_buffer ^= int(xor_value, 16)

while(username_len > 0):
	i += 1
	xor_value = GetXORValue(xor_value, username)
	encryption_buffer ^= int(xor_value, 16)
	username_len -= 1

full_key += str(encryption_buffer)
print(f"The serial is: {full_key}")