class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel="aeiouAEIOU"
        ans=""
        for i in s:
           if i in vowel:
              ans+=i
        b=ans[::-1]
        result=""
        j=0
        for i in s:
           if i in vowel:
              result+=b[j]
              j+=1
           else:
              result+=i
        return result