class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        cols = [0] * n
        rows = [0] * n
        boxes = [0] * n

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1

                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & boxes[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                boxes[(r // 3) * 3 + (c // 3)] |= (1 << val)
        
        return True