class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if  needle==haystack[i:i+len(needle)]:
                 return i
        return -1