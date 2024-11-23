class DecryptionUtils:
    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'
        """
        grid = [[''] * len(encrypted_text) for _ in range(rails)]
    
        rail = 0
        direction = 1
        for char in encrypted_text:
            grid[rail][col] = char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
    
        plaintext = ''
        rail = 0
        direction = 1
        for col in range(len(encrypted_text)):
            plaintext += grid[rail][col]
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
    
        return plaintext