class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        final=[]
        zero=[]
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                final.append(nums[i])
            else:
                zero.append(nums[i])
        final.extend(zero)
        for i in range(n):
            nums[i] = final[i]
        
        