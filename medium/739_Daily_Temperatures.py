class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexes = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()                   
            indexes[i] = stack[-1][0] - i if stack else 0
            stack.append((i, temperatures[i]))
        return indexes
