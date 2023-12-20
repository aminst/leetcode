class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for x, v in zip(position, speed):
            pairs.append((x, v))
        pairs = sorted(pairs, reverse=True)

        times = []
        prev_reaching_time = None
        for pair in pairs:
            if not prev_reaching_time:
                times.append(pair)
                prev_reaching_time = (target - pair[0]) / pair[1]
            elif (target - pair[0]) / pair[1] > prev_reaching_time:
                times.append(pair)
                prev_reaching_time = (target - pair[0]) / pair[1]
        return len(times)

