class Solution:
    def is_edge(self, board: List[List[str]], x, y):
        return x == 0 or y == 0 or x == len(board) - 1 or y == len(board[0]) - 1

    def convert_edge_connected(self, board: List[List[str]], x, y):
        if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
            return
        if board[x][y] == 'X' or board[x][y] == 'N':
            return
        if board[x][y] == 'O':
            board[x][y] = 'N'
        
        self.convert_edge_connected(board, x-1, y)
        self.convert_edge_connected(board, x+1, y)
        self.convert_edge_connected(board, x, y-1)
        self.convert_edge_connected(board, x, y+1)

    def convert_not_edge_connected(self, board: List[List[str]]):
        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if el == 'O':
                    board[i][j] = 'X'

    def revert_edge_connected(self, board: List[List[str]]):
        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if el == 'N':
                    board[i][j] = 'O'

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if el == 'O' and self.is_edge(board, i, j):
                    self.convert_edge_connected(board, i, j)
        self.convert_not_edge_connected(board)
        self.revert_edge_connected(board)
