class DecryptionUtils:
    def rail_fence_decipher(ciphertext, num_rails):
        # Create an empty grid with the specified number of rails
        grid = [[''] * len(ciphertext) for _ in range(num_rails)]
    
        # Fill the grid with the ciphertext characters
        rail = 0
        direction = 1
        for char in ciphertext:
            grid[rail][col] = char
            rail += direction
            if rail == 0 or rail == num_rails - 1:
                direction *= -1
    
        # Read the plaintext from the grid
        plaintext = ''
        rail = 0
        direction = 1
        for col in range(len(ciphertext)):
            plaintext += grid[rail][col]
            rail += direction
            if rail == 0 or rail == num_rails - 1:
                direction *= -1
    
        return plaintext