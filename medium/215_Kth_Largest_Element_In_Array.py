class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minimum = min(nums)
        maximum = max(nums)
        buckets = [0] * (maximum - minimum + 1)
        for num in nums:
            buckets[num - minimum] += 1
        count = 0
        for i in range(len(buckets) - 1, -1, -1):
            count += buckets[i]
            if count >= k:
                return i + minimum
