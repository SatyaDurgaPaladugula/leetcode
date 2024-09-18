class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
       
        for i in range(len(nums)):
            sum=0
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    sum+=1
               
            l.append(sum)
        return l
