import random

class Solution:
    def modifyString(self, s: str) -> str:
        mapping = {}
        for i in range(len(s)):
            if s[i] != "?":
                mapping[i] = s[i]
            else:
                mapping[i] = "?"
    
        ans = ""
        for i in range(len(s)):
            if s[i].isalpha():
                ans += s[i]
                continue
            avoid = [mapping.get(i-1,""),mapping.get(i,""),mapping.get(i+1,"")]
            while True:
                tmp = random.choice("abcdegfhijklmnopqrstuvwxyz")
                if tmp not in avoid:
                    mapping[i] = tmp
                    ans += tmp
                    break
                continue
        
        return ans