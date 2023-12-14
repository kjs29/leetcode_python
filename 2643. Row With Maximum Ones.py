class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        ans = [0,0]
        max_count = 0
        
        for r in range(len(mat)):
            
            if mat[r].count(1) == max_count:
                ans[0] = min(ans[0], r)
            
            if mat[r].count(1) > max_count:
                max_count = mat[r].count(1)
                ans[0] = r
                ans[1] = max_count

        return ans