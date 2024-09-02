class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=10:
            temp=num
            sum=0
            while temp>0:
               d=temp%10
               sum+=d
               temp//=10
            num=sum
        
        return num
