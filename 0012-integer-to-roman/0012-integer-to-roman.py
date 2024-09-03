class Solution:
    def intToRoman(self, num: int) -> str:
        if num > 3999:
            return "Input exceeds the limit for standard Roman numerals"
        
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        i = 0

        while num > 0:
            div = num // value[i]
            num %= value[i]
            while div > 0:
                roman += symbol[i]
                div -= 1
            i += 1
        
        return roman
