from heapq import *

class MedianFinder:

    def __init__(self):
        self.small = []
        heapify(self.small)      
        self.big = []
        heapify(self.big)

    def addNum(self, num: int) -> None:
      if len(self.small) == len(self.big):
        heappush(self.big, -heappushpop(self.small, -num))
      else:
        heappush(self.small, -heappushpop(self.big, num))

    def findMedian(self) -> float:
      if len(self.small) == len(self.big):
        return (-self.small[0] + self.big[0]) / 2
      else:
        return self.big[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
