def vigenere_decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    key = key.upper()
    key_length = len(key)
    key_indices = [alphabet.index(k) for k in key]

    key_index = 0
    for char in ciphertext:
        if char.upper() in alphabet:
            offset = key_indices[key_index % key_length]
            decrypted_index = (alphabet.index(char.upper()) - offset) % 26
            decrypted_char = alphabet[decrypted_index]
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char  # preserva pontuação e espaços

    return plaintext

# Mensagem e chave
ciphertext = "UJAHLGYJSXASVWUWKSJ:VWKVWSSFLAYMAVSVW.SUZSNWWUJAHLGUDSKKAUS"
key = "SSSSSSSSSWS"

# Decifrando
decrypted = vigenere_decrypt(ciphertext, key)
print("Mensagem decifrada:")
print(decrypted)
