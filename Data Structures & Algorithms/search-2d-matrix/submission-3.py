class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vec = []
        for row in matrix:
            for col in row:
                vec.append(col)
        
        l, r = 0, len(vec) - 1
        while l <= r:
            k = l + ((r - l) // 2)
            if vec[k] == target:
                return True
            
            elif vec[k] < target:
                l = k + 1
            
            elif vec[k] > target:
                r = k - 1
            else:
                return False
        return False