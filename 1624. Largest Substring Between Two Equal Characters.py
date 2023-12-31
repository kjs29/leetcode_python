class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        ans = -1
        
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = [i]
            else:
                seen[s[i]].append(i)
                ans = max(ans, seen[s[i]][-1] - seen[s[i]][0] - 1)

        return ans