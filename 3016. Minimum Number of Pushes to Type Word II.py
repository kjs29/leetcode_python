class Solution:
    def minimumPushes(self, word: str) -> int:
        
        res = []
        for ch in set(word):
            res.append([ch, word.count(ch)])
        res.sort(key=lambda x:x[1], reverse=True)

        ans = 0
        
        for i in range(len(res)):
            _,freq = res[i]
            quotient = 1 + (i // 8)
            ans += (freq * quotient)
        
        return ans