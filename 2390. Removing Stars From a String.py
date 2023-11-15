class Solution:
    def removeStars(self, s: str) -> str:
        ans = ""
        i = len(s) - 1
        c = 0   # tracks how many consecutive stars appear
        
        while i >= 0:
            if s[i] == "*": # if the current letter is a star
                c += 1
            else:
                if c == 0:  # if consecutive star counted prior to current letter is 0
                    ans += s[i]
                else:       # if consecutive stars appeared previously
                    c -= 1
            i -= 1

        return ans[::-1]