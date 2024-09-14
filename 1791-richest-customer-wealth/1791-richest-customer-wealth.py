class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
      
      max_wealth=0
      for i in range(len(accounts)):
         sum=0
         for j in range(len(accounts[i])):
            sum+=accounts[i][j]
            if max_wealth  <sum:
                max_wealth=sum

      return max_wealth
     
     
