class Solution:
    def countSegments(self, s: str) -> int:
        s1=s.split(" ")
        c=0
        for segment in s1:
            if segment:
                c+=1
        return c
