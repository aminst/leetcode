class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        def exists_without_repeat(x, y, curr_index, used_pos):
            if curr_index == len(word):
                return True            
            if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0]) - 1:
                return False
            if word[curr_index] == board[x][y] and (x, y) not in used_pos:
                used_pos.add((x, y))
                is_reachable = (
                    exists_without_repeat(x + 1, y, curr_index + 1, used_pos) or
                    exists_without_repeat(x - 1, y, curr_index + 1, used_pos) or
                    exists_without_repeat(x, y + 1, curr_index + 1, used_pos) or
                    exists_without_repeat(x, y - 1, curr_index + 1, used_pos)
                )
                used_pos.remove((x, y))
                return is_reachable
            return False

        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if exists_without_repeat(i, j, 0, set()):
                    return True
        return False
