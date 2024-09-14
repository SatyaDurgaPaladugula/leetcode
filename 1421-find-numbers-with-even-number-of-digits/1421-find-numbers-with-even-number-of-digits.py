class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count1=0
        l=[]
        for i in range(len(nums)):
            n=nums[i]
            count=0
            while n>0:
                d=n%10
                count+=1
                n//=10
        
            if count%2==0:
                count1+=1
        return count1
