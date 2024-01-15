class Solution:
    def sortString(self, s: str) -> str:

        s = list(s)
        fr = Counter(s)
        ans = ""
        alphabets = "abcdefghijklmnopqrstuvwxyz"

        while len(ans) < len(s):
            # op 1
            for ch in alphabets:
                if fr[ch] > 0:
                    ans += ch
                    fr[ch] -= 1
            # op 2
            for ch in alphabets[::-1]:
                if fr[ch] > 0:
                    ans += ch
                    fr[ch] -= 1
        
        return ans