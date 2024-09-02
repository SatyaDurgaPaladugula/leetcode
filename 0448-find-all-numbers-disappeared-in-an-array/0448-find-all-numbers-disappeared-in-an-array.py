class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
     
        n=len(nums)
        set_num=set(nums)
        l=[]
        for i in range(1,n+1):
            if i  not in set_num:
                l.append(i)
        return l