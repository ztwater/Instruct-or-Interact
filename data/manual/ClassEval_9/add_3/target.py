class BigNumCalculator:
    def add(self, num1, num2):
        # Convert the numbers to strings
        str1 = str(num1)
        str2 = str(num2)
        
        # Find the lengths of the strings
        len1 = len(str1)
        len2 = len(str2)
        
        # Make the lengths of the strings equal by adding leading zeros
        if len1 > len2:
            str2 = '0' * (len1 - len2) + str2
        elif len2 > len1:
            str1 = '0' * (len2 - len1) + str1
        
        # Initialize variables for the sum and carry
        sum_str = ''
        carry = 0
        
        # Iterate through the strings from right to left
        for i in range(len(str1)-1, -1, -1):
            # Convert the current digits to integers
            digit1 = int(str1[i])
            digit2 = int(str2[i])
            
            # Add the digits and the carry
            digit_sum = digit1 + digit2 + carry
            
            # Update the sum and carry
            sum_str = str(digit_sum % 10) + sum_str
            carry = digit_sum // 10
        
        # Add the final carry if it is not zero
        if carry != 0:
            sum_str = str(carry) + sum_str
        
        # Return the sum as a string
        return sum_str