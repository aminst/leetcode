class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        fib = [None] * (n + 1)
        fib[0] = 0
        fib[1] = 1
        fib[2] = 2
        for i in range(3, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]
