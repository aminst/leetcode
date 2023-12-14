class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(n)
        if n < 0:
            x = 1.0/x
            n = (-1)*n
        if n == 0:
            return 1
        if n == 1:
            return x

        p1 = self.myPow(x, n//2)
        if n%2 == 0:
            return p1*p1
        else:
            return x*p1*p1
