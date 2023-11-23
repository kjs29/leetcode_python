class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        maxLocal = [[0 for _ in range(N-2)] for _ in range(N-2)]
        
        for r in range(N-2):
            for c in range(N-2):
                sub_max = 0     # max number in each 3x3 submatrix
                sub_max = max(
                    grid[r][c],grid[r][c+1],grid[r][c+2],       # top row
                    grid[r+1][c],grid[r+1][c+1],grid[r+1][c+2], # middle row
                    grid[r+2][c],grid[r+2][c+1],grid[r+2][c+2]  # bottom row
                )
                maxLocal[r][c] = sub_max
                
        return maxLocal