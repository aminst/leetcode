class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [None] * len(nums)
        def max_up_to_index(index):
            if mem[index] != None:
                return mem[index]

            if index == 0:
                mem[index] = nums[index]
                return mem[index]
            if index == -1:
                return 0
            
            mem[index] = max(
                max_up_to_index(index - 1),
                max_up_to_index(index - 2) + nums[index]
            )
            return mem[index]
        return max_up_to_index(len(nums) - 1)
