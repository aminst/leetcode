class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": 
            return "0"
        result = [0] * (len(num1) + len(num2))

        num1, num2 = num1[::-1], num2[::-1]
        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                multi = int(d1) * int(d2)
                result[i + j] += multi
                result[i + j + 1] += result[i + j] // 10
                result[i + j] = result[i + j] % 10
        start = 0
        result = result[::-1]
        for i in range(len(result)):
            if result[i] != 0:
                start = i
                break
        return "".join(map(str, result[start:]))
        
