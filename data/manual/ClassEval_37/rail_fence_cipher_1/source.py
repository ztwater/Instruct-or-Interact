class EncryptionUtils:
    def rail_fence_cipher(plaintext, num_rails):
        # Create a list of empty strings to represent each rail
        rails = [''] * num_rails
    
        # Initialize variables for tracking the current rail and direction
        rail = 0
        direction = 1
    
        # Iterate through each character in the plaintext
        for char in plaintext:
            # Add the character to the current rail
            rails[rail] += char
    
            # Update the current rail and direction
            rail += direction
    
            # Reverse the direction if we reach the first or last rail
            if rail == 0 or rail == num_rails - 1:
                direction *= -1
    
        # Concatenate the strings from each rail to form the ciphertext
        ciphertext = ''.join(rails)
    
        return ciphertext