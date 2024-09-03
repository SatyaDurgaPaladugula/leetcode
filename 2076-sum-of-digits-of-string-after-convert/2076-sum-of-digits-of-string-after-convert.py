class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ""
        for i in s:
            ans += str(ord(i) - ord('a') + 1)
        
        for _ in range(k):
            sum_digits = 0
            for char in ans:
                sum_digits += int(char)
            ans = str(sum_digits)
        
        return int(ans)
