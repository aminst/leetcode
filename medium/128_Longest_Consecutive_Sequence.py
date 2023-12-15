class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 in nums_set:
                continue
            next_num = num + 1
            while next_num in nums_set:
                next_num += 1
            max_len = max(max_len, next_num-num)
        return max_len
