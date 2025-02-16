class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        sum=0
        for i in range(len(hours)):
            if hours[i]>=target:
                sum+=1
        return sum