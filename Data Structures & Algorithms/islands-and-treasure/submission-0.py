class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def findTreasure(grid):
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        q.append([i, j])
                        visit.add((i, j))
        
        def lvlchecker(r, c):
            if (min(r, c) < 0 or r == m or c == n or
                (r, c) in visit or grid[r][c] == -1
            ):
                return 
            visit.add((r, c))
            q.append([r, c])
        
        findTreasure(grid)
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                lvlchecker(r + 1, c)
                lvlchecker(r - 1, c)
                lvlchecker(r, c + 1)
                lvlchecker(r, c - 1)
            dist += 1


        