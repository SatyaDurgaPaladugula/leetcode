class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp=x
        sum=0
        while temp>0:
            d=temp%10
            sum+=d
            temp//=10
        if x%sum==0:
            return sum
        return -1