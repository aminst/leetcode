class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        answer_set = set()
        current = []
        def generate(opened, closed):
            if opened == n and closed == n:
                answer_set.add("".join(current))
                return
            if opened < n:
                current.append("(")
                generate(opened + 1, closed)
                current.pop()
            if closed < opened:
                current.append(")")
                generate(opened, closed + 1)
                current.pop()

        generate(0, 0)
        return answer_set
