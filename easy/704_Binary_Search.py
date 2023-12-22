class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid_index = (l + r) // 2
            mid = nums[mid_index]
            if mid == target:
                return mid_index
            if mid < target:
                l = mid_index + 1
            if mid > target:
                r = mid_index - 1
        return -1
