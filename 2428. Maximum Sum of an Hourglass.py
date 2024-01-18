class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)       #row
        n = len(grid[0])    #col

        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                f = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                s = grid[i+1][j+1]
                t = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                ans = max(ans, f+s+t)
        
        return ans