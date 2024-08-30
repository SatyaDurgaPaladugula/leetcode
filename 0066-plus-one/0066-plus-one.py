class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(map(str, digits))
        b=int(s)+1
        b1=str(b)
        return list(map(int, b1))