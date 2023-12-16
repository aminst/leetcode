class Solution:
    def get_digit_squared_sum(self, n: int) -> int:
        squared_sum = 0
        while n != 0:
            cur_digit = n % 10
            squared_sum += cur_digit * cur_digit
            n = n//10
        return squared_sum

    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            n = self.get_digit_squared_sum(n)
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
