class DecryptionUtils:
    def vigenere_decipher(ciphertext, key):
        plaintext = ""
        key_length = len(key)
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            if char.isalpha():
                key_char = key[i % key_length]
                if char.isupper():
                    plaintext += chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
                else:
                    plaintext += chr((ord(char) - ord(key_char) + 26) % 26 + ord('a'))
            else:
                plaintext += char
        return plaintext