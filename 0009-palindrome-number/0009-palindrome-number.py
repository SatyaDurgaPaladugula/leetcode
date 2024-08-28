class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        while temp>0:
            d=temp%10
            rev=(rev*10)+d
            temp//=10
        return rev==x