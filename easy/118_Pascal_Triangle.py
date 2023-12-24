class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        prev = self.generate(numRows - 1)
        last = prev[-1]
        new_row = [1]
        for i, num in enumerate(last[:-1]):
            new_row.append(num + last[i + 1])
        new_row.append(1)
        prev.append(new_row)
        return prev
