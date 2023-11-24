class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i_s = 0
        i_t = 0
        
        while i_s < len(s) and i_t < len(t):
            if s[i_s] == t[i_t]:
                i_s += 1
                i_t += 1
            else:
                i_t += 1
        
        if i_s != len(s):
            return False

        return True