class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = (len(nums) * (len(nums) + 1)) // 2
        current_sum = 0
        for num in nums:
            current_sum += num
        return expected_sum - current_sum
