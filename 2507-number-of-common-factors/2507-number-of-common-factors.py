class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        l=[]
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                l.append(i)
        return len(l)