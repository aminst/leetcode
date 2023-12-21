class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find_all_connected(x, y):
            if x == len(grid) or x == -1 or y == len(grid[0]) or y == -1: return
            if grid[x][y] != "1": return
            grid[x][y] = "$"
            find_all_connected(x + 1, y)
            find_all_connected(x - 1, y)
            find_all_connected(x, y + 1)
            find_all_connected(x, y - 1)

        count = 0
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if el != "1": continue
                find_all_connected(i, j)
                count += 1
        
        return count
