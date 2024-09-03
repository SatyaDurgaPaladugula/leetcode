class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary with Roman numeral values
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize total sum
        total = 0

        # Traverse through the Roman numeral string
        for i in range(len(s)):
            # If the next numeral is larger, subtract the current numeral
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            else:
                # Otherwise, add the current numeral
                total += roman_values[s[i]]
                
        return total
