class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        set_num=set(nums)
        for i in range(1,n+1):
            if i  not in set_num:
                return i
        return n+1