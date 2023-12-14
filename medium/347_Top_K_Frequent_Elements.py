class Solution:
    def getCount(self, nums: List[int]) -> Dict:
        val_to_count = dict()
        for num in nums:
            if num not in val_to_count:
                val_to_count[num] = 0
            val_to_count[num] += 1
        return val_to_count

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_to_count = self.getCount(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for val, count in val_to_count.items():
            buckets[count].append(val)            
        top_k = list()
        count = 0
        for val_list in reversed(buckets):
            if count >= k:
                break
            count += len(val_list)
            top_k += val_list
        return top_k
