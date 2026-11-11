class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        visit = set()
        bana = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] > 0:
                    bana += 1
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        
        if bana == 0:
            return 0
        if len(q) == 0:
            return -1

        def rotted(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == 0 or (r, c) in visit:
                return
            q.append([r, c])
            visit.add((r, c))
        
        minutes = 0
        while q:
            for b in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = minutes
                rotted(i - 1, j)
                rotted(i + 1, j)
                rotted(i, j + 1)
                rotted(i, j - 1)

            
            minutes += 1
        
        if len(visit) != bana:
            return -1
        else:
            return minutes - 1

