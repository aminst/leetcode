class Solution:

    def is_operator(self, ch) -> bool:
        return ch == '*' or ch == '/' or ch == '+' or ch == '-'
    
    def apply(self, operator, x, y):
        if operator == '*':
            return x * y
        if operator == '/':
            return int(x / y)
        if operator == '+':
            return x + y
        if operator == '-':
            return x - y

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_operator(token):
                y = stack.pop()
                x = stack.pop()
                stack.append(self.apply(token, x, y))
                print(stack[-1])
            else:
                stack.append(int(token))
        return stack[0]
