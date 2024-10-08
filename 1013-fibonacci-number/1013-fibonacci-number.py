class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b if n > 0 else a
      