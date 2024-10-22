class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dici={}
        rev={}
        iso=True
        for i in range(len(s)):
            ch1=s[i]
            ch2=t[i]
            if ch1 not in dici and ch2 not in rev:
                dici[ch1]=ch2
                rev[ch2]=ch1
            elif (ch1 in dici and dici[ch1]!=ch2):
                iso=False
                break
            elif (ch2 in rev and rev[ch2]!=ch1):
                iso=False
                break
        return iso
        