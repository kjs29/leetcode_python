class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        
        for word in words:
            first = set("qwertyuiop")
            second = set("asdfghjkl")
            third = set("zxcvbnm")
            w_set = set(word.lower())
            
            if w_set.issubset(first) or w_set.issubset(second) or w_set.issubset(third):
                ans.append(word)
        
        return ans