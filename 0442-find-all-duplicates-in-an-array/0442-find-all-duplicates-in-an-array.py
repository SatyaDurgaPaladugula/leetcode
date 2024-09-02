class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen=set()
        duplicate=set()
        for num in nums:
            if num in seen:
                duplicate.add(num)
            else:
                seen.add(num)
        return duplicate