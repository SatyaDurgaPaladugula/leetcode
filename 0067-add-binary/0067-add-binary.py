class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1=int(a,2)
        a2=int(b,2)
        a3=bin(a1+a2)
        return a3[2:]
