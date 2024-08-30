class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        # Iterate through each number from 0 to n
        for i in range(n + 1):
            # Count the number of 1s in the binary representation of i
            count = bin(i).count('1')
            # Append the count to the result list
            result.append(count)
        return result