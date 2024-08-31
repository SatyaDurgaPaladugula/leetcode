class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt=math.isqrt(num)
        return  sqrt*sqrt==num
