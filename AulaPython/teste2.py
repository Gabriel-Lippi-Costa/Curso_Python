hex_string = "0400242d05612905380115301d1701247c0a3d1611261b65143c04103e20223c1066002230262408"
bytes_data = bytes.fromhex(hex_string)

# Testar chaves de 0x00 até 0xFF
for key in range(256):
    decoded = ''.join([chr(byte ^ key) for byte in bytes_data])
    print(f"Chave: {key:#04x}, Decodificado: {decoded}")
