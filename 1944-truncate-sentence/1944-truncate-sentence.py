class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1=s.split()
        a=" ".join(s1[:k])
        return a