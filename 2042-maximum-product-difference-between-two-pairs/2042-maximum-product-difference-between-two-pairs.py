class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        arr=sorted(nums)
       
        d1 = arr[-1] * arr[-2]  
        d2 = arr[0] * arr[1] 
            
        return d1-d2
