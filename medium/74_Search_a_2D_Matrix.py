class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid_index = (l + r) // 2
            mid_index_x = mid_index // len(matrix[0])
            mid_index_y = mid_index % len(matrix[0])
            mid = matrix[mid_index_x][mid_index_y]
            if target == mid:
                return True
            elif target < mid:
                r = mid_index - 1
            else:
                l = mid_index + 1
        return False
