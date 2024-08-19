class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
     ans=""
     ans1=""
     for i in range(len(word1)):
         ans+=(word1[i])
     for i in range(len(word2)):
         ans1+=(word2[i])
     
     return ans == ans1 