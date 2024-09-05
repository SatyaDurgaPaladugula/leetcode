class Solution:
    def secondHighest(self, s: str) -> int:
        l=set()
        for i in s:
            if i.isdigit():
                l.add(int(i))
        sorted_digit=sorted(l)
        if len(sorted_digit) < 2:
            return -1
        return sorted_digit[-2]