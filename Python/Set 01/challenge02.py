def cg02_fixed_xor(value1, value2):
    xor_int = int(value1, 16)^int(value2, 16)
    xor_hex = hex(xor_int)


    return str(xor_hex)[2:-1]