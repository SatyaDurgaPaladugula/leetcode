class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a = []
        for op in operations:
            if op == '+':
                a.append(a[-1] + a[-2])
            elif op == 'D':
                a.append(2 * a[-1])
            elif op == 'C':
                a.pop()
            else:
                a.append(int(op))
        return sum(a)