class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]<nums[j]:
                    l.append(nums[j]-nums[i])
        return max(l) if l else -1
