class Solution:
    def get_hours_taken(self, piles, k):
        if k == 0:
            return 10**12
        count = 0
        for pile in piles:
            count += (pile - 1) // k + 1
        return count

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            count = self.get_hours_taken(piles, mid)
            if count <= h:
                r = mid
            if count > h:
                l = mid + 1
        return l
