class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        
        def dfs(r, l):
            if min(r, l) < 0 or r == m or l == n or board[r][l] != "O":
                return
            board[r][l] = "T"
            dfs(r + 1, l)
            dfs(r - 1, l)
            dfs(r, l + 1)
            dfs(r, l - 1)
        
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n-1)
        
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
