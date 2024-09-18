class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        re=0
        for i in range(len(colors)):
            for j in range(i,len(colors)):
               if colors[i]!=colors[j]:
                   result=abs(i-j)
                   re=max(result,re)
        return re