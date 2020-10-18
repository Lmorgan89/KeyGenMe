serial_prefix = "br0"
serial_suffix = "ken"
encryption_key = [0x40, 0x5E, 0x2A, 0x52, 0x24, 0x46, 0x56, 0x54, 0x25, 0x40, 0x00]
key_position_offset = int(hex(ord('\n'))[2:], 16)

input_name = list(input("Enter Name: "))
input_name_length = len(input_name)

i = 0
val1 = 0
val2 = 0
val3 = 0
while(i < input_name_length):
    current_char = int(hex(ord(input_name[i]))[2:], 16)
    val2 += current_char ^ (encryption_key[(current_char % key_position_offset)])
    val1 += (encryption_key[i]) * current_char + 0xefef
    
    itterator2 = 0
    while(itterator2 < input_name_length):
        cur_char = int(hex(ord(input_name[itterator2]))[2:], 16)
        val3 = (cur_char * cur_char + val1) - val2
        itterator2 += 1
    i += 1

print(f"Serial: {serial_prefix}-{val1}-{val2}{val3}-{serial_suffix}")