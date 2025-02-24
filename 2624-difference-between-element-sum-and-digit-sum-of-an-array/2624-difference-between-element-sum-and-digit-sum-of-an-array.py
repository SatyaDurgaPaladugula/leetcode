class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum2=sum(nums)
        sum1=0
        for num in nums:
            while num>0:
                sum1+=num%10
                num//=10
        return abs(sum2-sum1)

