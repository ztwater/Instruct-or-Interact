class DecryptionUtils:
    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        plaintext = ""
        key_length = len(self.key)
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            if char.isalpha():
                key_char = self.key[i % key_length]
                if char.isupper():
                    plaintext += chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
                else:
                    plaintext += chr((ord(char) - ord(key_char) + 26) % 26 + ord('a'))
            else:
                plaintext += char
        return plaintext