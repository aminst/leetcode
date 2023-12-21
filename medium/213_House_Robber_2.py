class Solution:
    def rob(self, nums: List[int]) -> int:
        mem_with_first = [None] * len(nums)
        mem_without_first = [None] * len(nums)
        def max_to_index(index, includes_first):
            if index == 0:
                return nums[0] if includes_first else 0
            if index < 0:
                return 0
            
            if includes_first and mem_with_first[index] != None:
                return mem_with_first[index]
            if not includes_first and mem_without_first[index] != None:
                return mem_without_first[index]

            curr_max = max(
                max_to_index(index - 1, includes_first),
                max_to_index(index - 2, includes_first) + nums[index]
            )
            if includes_first:
                mem_with_first[index] = curr_max
            else:
                mem_without_first[index] = curr_max
            return curr_max

        index = len(nums) - 1
        return max(
                    max_to_index(index - 1, True),
                    max_to_index(index - 2, False) + nums[index],
                    max_to_index(index - 2, True)
                )
