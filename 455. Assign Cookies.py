class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        
        g.sort()
        s.sort()
        i2 = len(s) - 1
        ans = 0
        
        for i1 in range(len(g)-1,-1,-1):
            if g[i1] <= s[i2]:
                ans += 1
                i2 -= 1
            if i2 == -1:
                return ans
        
        return ans