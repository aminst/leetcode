class Solution:
    def isSegmentValid(self, segment):
        cells = [cel for cel in segment if cel != '.']
        return len(set(cells)) == len(cells)

    def isRowsValid(self, board) -> bool:
        for row in board:
            if not self.isSegmentValid(row):
                return False
        return True
    
    def isColsValid(self, board) -> bool:
        for col in zip(*board):
            if not self.isSegmentValid(col):
                return False
        return True

    def isSquaresValid(self, board) -> bool:
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isSegmentValid(square):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowsValid(board) and self.isColsValid(board) and self.isSquaresValid(board)
