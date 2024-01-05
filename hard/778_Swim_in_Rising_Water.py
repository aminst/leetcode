import math
class Solution:

    def can_reach(self, x, y, max_val, visited, grid):
        if (
            x < 0 or
            y < 0 or
            x >= len(grid) or
            y >= len(grid[0]) or
            grid[x][y] > max_val or
            visited[x][y]
        ):
            return False
        if x == len(grid) - 1 and y == len(grid[0]) - 1: return True
        visited[x][y] = True
        return (
            self.can_reach(x + 1, y, max_val, visited, grid) or
            self.can_reach(x - 1, y, max_val, visited, grid) or
            self.can_reach(x, y + 1, max_val, visited, grid) or
            self.can_reach(x, y - 1, max_val, visited, grid)
        )


    def swimInWater(self, grid: List[List[int]]) -> int:
        l = 0
        r = 2500
        while l < r:
            visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
            mid = (l + r) // 2
            if self.can_reach(0, 0, mid, visited, grid):
                r = mid
            else:
                l = mid + 1
        return l
