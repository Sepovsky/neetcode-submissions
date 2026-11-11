class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def hlp(heights, A=1):
            ROW, COL = len(heights), len(heights[0])
            ridx = ROW-1 if A == 1 else 0
            cidx = COL-1 if A == 1 else 0
            q = deque()
            visit = set()
            for c in range(COL):
                q.append([ridx, c])
                visit.add((ridx, c))
            
            for r in range(ROW):
                q.append([r, cidx])
                visit.add((r, cidx))
            
            def checkh(i, j, pre_val):
                if min(i, j) < 0 or j == COL or i == ROW or pre_val > heights[i][j] or (i, j) in visit:
                    return
                q.append([i, j])
                visit.add((i, j))
            
            while q:
                r, c = q.popleft()
                checkh(r + 1, c, heights[r][c])
                checkh(r - 1, c, heights[r][c])
                checkh(r, c + 1, heights[r][c])  
                checkh(r, c - 1, heights[r][c])
            return visit
        
        a = hlp(heights, A=1)
        p = hlp(heights, A=0)
        res = [[r, c] for r, c in p if (r, c) in a]
        return res


