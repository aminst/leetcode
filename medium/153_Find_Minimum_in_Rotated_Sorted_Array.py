class Solution:
    def binSearch(self, nums, start, end):
        if start == end:
            return 0
        if end < start:
            return -1
        mid = (start + end + 1) // 2
        if nums[mid] < nums[mid-1]:
            return mid
        if nums[mid] < nums[start]:
            return self.binSearch(nums, start, mid-1)
        else:
            return self.binSearch(nums, mid, end)


    def findMin(self, nums: List[int]) -> int:
        return nums[self.binSearch(nums, 0, len(nums)-1)]
