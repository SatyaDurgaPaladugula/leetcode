class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul=1
        sum=0
       
        while n>0:
            d=n%10
            mul*=d
            sum+=d
            n//=10
        return mul-sum