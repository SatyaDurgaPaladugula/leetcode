class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        set_num=set(nums)
        for i in range(n+1):
            if i  not in set_num:
                return i
        