from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        times = self.map[key]
        l, r = 0, len(times) - 1
        while l <= r:
            mid_index = (l + r) // 2
            mid_time, mid_val = times[mid_index]
            if mid_time == timestamp:
                return mid_val
            if mid_time < timestamp:
                l = mid_index + 1
            if mid_time > timestamp:
                r = mid_index - 1
        if l >= 1:
            return times[l - 1][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


"""
set(key, value, timestamp): strictly increasing
get(key, timestamp):
    * closest smaller or equal timestamp_prev to timestamp -> value
    * not any: return ""

1 <= key, value <= 100 and small english letters

set foo, bar, 1
get foo, 1 -> bar
get foo, 3 -> bar
set foo, bar2, 4
get foo, 4 -> bar2
get foo, 5 -> bar2

[1, 4] -> binary search here

Solution:
map of key to list of time and value
binary search to either find that or we will return the one smaller than that.

"""
