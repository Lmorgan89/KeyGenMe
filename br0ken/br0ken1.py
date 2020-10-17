internal_password = "QbTTx1sE"
cracked_password = ''

for c in internal_password:
	character = int(hex(ord(c))[2:], 16) - 1
	cracked_password += chr(character)

print(f"Password: {cracked_password}")


input_name = list(input("Name, 2-10 chars: "))
name_length = len(input_name)
while (name_length > 10 or name_length < 2):
	input_name = list(input("Name, 2-10 chars: "))

i = 0
serial = 0
while(i < name_length):
	serial += int(hex(ord(input_name[i]))[2:], 16) - 1
	i +=1

print(f"Your serial should be: {serial-1}")