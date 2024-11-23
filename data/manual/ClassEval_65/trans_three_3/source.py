class NumberWordFormatter:
    def trans_three(number):
        # Define the words for each digit
        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
        # Convert the number to a string
        number_str = str(number)
    
        # Get the digits
        hundreds_digit = int(number_str[0])
        tens_digit = int(number_str[1])
        ones_digit = int(number_str[2])
    
        # Convert each digit to words
        hundreds_word = ones[hundreds_digit] + " hundred" if hundreds_digit != 0 else ""
        tens_word = tens[tens_digit]
        ones_word = ones[ones_digit]
    
        # Handle special cases for teens
        if tens_digit == 1:
            tens_word = teens[ones_digit]
            ones_word = ""
    
        # Combine the words and return the result
        return hundreds_word + " " + tens_word + " " + ones_word