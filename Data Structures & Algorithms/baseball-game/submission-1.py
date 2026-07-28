class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum1 = []
        for i in range(len(operations)):
            if operations[i] == "C":
                sum1.pop()
            elif operations[i] == "+":
                sum1.append(sum1[-1] + sum1[-2])
            elif operations[i] == "D":
                sum1.append(sum1[-1] * 2)
            else:
                sum1.append(int(operations[i]))
        return sum(sum1)