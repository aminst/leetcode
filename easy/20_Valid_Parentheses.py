class Solution:
    def is_opening(self, ch):
        return ch == '(' or ch == '[' or ch == '{'

    def get_opening_of_ch(self, ch):
        if ch == ')': return '('
        elif ch == '}': return '{'
        elif ch == ']': return '['
        else: return None

    def close_with_char(self, stack, ch):
        while stack:
            current_ch = stack.pop()
            if current_ch != self.get_opening_of_ch(ch):
                return False
            else:
                return True


    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if self.is_opening(ch):
                stack.append(ch)
            else:
                is_valid = self.close_with_char(stack, ch)
                if not is_valid:
                    return False
        return len(stack) == 0

