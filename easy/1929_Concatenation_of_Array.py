class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        curr_length = len(nums)
        for i in range(curr_length):
            nums.append(nums[i])
        return nums
