class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        window = list(s[:3])
        ans = 1 if len(set(window)) == 3 else 0
        
        for i in range(3, len(s)):

            if s[i] != window[1] and s[i] != window[2] and window[1] != window[2]:
                ans += 1
            
            window.pop(0)
            window.append(s[i])

        return ans
    
# Another solution
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        ans = 0        
        
        for i in range(2, len(s)):
            if s[i-2] != s[i-1] and s[i-1] != s[i] and s[i-2] != s[i]:
                ans += 1

        return ans