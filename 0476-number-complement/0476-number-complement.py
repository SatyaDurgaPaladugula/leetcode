class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)[2:]
        result=''
        for i in b:
            if i=='0':
                 result+='1'
            else:
                 result+='0'
        return int(result,2)