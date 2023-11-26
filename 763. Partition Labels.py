class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen_map = {}
        for i in range(len(s)):
            last_seen_map[s[i]] = i
        
        last_idx = 0    # last seen index
        sum_seen = 0    # total number of characters that appended to answer
        ans = []
        for i in range(len(s)):
            ch = s[i]
            last_idx = max(last_idx, last_seen_map[ch])
            
            if i == last_idx:   # if current index is the last index in the current partition
                if not ans:
                    ans.append(i+1)
                    sum_seen = ans[-1]
                else:
                    ans.append(i + 1 - sum_seen)
                    sum_seen += ans[-1]

        return ans