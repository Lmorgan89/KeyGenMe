for x in range(1000000,9999999):
	input_password = list(str(x))
	i = 0
	value = 0
	while (i < 6):
		pw_char = int(hex(ord(input_password[i]))[2:], 16)
		value += (pw_char * 3 - 0x28) * pw_char
		i += 1

	div_10 = value % 10
	if(div_10 == 0):
		print(f"Found: {x}")