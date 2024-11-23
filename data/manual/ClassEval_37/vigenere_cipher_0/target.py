class EncryptionUtils:
    def vigenere_cipher(self, plaintext):
        ciphertext = ""
        key = self.key.upper()
        key_length = len(key)
        for i in range(len(plaintext)):
            char = plaintext[i]
            if char.isalpha():
                if char.isupper():
                    ciphertext += chr((ord(char) + ord(key[i % key_length]) - 2 * ord('A')) % 26 + ord('A'))
                else:
                    ciphertext += chr((ord(char) + ord(key[i % key_length]) - 2 * ord('a')) % 26 + ord('a'))
            else:
                ciphertext += char
        return ciphertext