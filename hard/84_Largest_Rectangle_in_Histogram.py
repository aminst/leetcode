class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        current_max = 0
        heights.append(0)
        for i, height in enumerate(heights):
                start = i
                while stack and height < stack[-1][0]:
                    top_height, top_index = stack.pop()
                    current_max = max(current_max, top_height * (i - top_index))
                    start = top_index
                stack.append((height, start))
        return current_max
