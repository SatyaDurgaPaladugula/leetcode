from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mins = nums[0]  # Initialize with the first element of the list
        
        for num in nums:
            
            if abs(num) < abs(mins):
                mins = num
            # If there's a tie, choose the positive number
            elif abs(num) == abs(mins) and num > mins:
                mins = num
        
        return mins
