class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left, right + 1):
            temp = i
            is_self_dividing = True
            while temp > 0:
                d = temp % 10
                if d == 0 or i % d != 0:
                    is_self_dividing = False
                    break
                temp //= 10
            if is_self_dividing:
                l.append(i)
        return l
