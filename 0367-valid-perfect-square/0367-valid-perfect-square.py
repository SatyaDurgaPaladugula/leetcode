class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        i = 0
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False
