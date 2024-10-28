class Solution:
    def repeatedCharacter(self, s: str) -> str:
       freq={}
       for i in s:
           if i in freq:
               return i
           else:
               freq[i]=1
    