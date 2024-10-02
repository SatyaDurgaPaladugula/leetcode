class Solution:
    def trailingZeroes(self, n: int) -> int:
        #fact=1
        #for i in range(1,n+1):
            #fact=fact*i
       # return str(fact).count('0')
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count