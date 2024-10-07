class Solution:
    def replaceDigits(self, s: str) -> str:
        l=""
        for i in range(len(s)):
            if s[i].isdigit():
                a=ord(s[i-1])+int(s[i])
                l+=chr(a)
            else:
                l+=(s[i])
        return l
                
               