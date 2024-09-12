class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l=[]
        sum=0
        for i in range(n):
            l.append(start+2*i)
            
        for i in range(len(l)):
             sum^=l[i]
        return sum

        
        
