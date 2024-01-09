class Solution:
    def get_area(self, heights, start, end):
        min_height = min(heights[start], heights[end])
        return min_height * (end - start)

    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = self.get_area(height, l, r)
        while l < r:
            max_area = max(max_area, self.get_area(height, l, r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
