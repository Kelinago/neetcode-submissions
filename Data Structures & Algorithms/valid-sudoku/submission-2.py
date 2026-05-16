class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            c = r
            row = [board[r][i] for i in range(9) if board[r][i] != '.']
            col = [board[i][c] for i in range(9) if board[i][c] != '.']
            if len(set(row)) != len(row) or len(set(col)) != len(col):
                return False
        for c in range(0, 9, 3):
            for r in range(0, 9, 3):
                box = []
                for i in range(r, r + 3):
                    box.extend([
                        n for n in board[i][c: c + 3]
                        if n != '.'
                    ])
                if len(set(box)) != len(box):
                    return False
        return True