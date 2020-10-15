username = input("Enter Username: ").upper()
key = "SnD-"
name_length = len(username)
encryption_key = 0x1749

i=0
buff=0
while(name_length > 0):
	if(username[i] != ' '):
		name_char = str(hex(ord(username[i]))[2:])
		buff += (int(name_char, 16) * encryption_key) -1
	i += 1
	name_length -= 1

key += str(buff)
print(f"The key is: {key}")