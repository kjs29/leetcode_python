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
    
# Another solution
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        
        for word in words:
            first = set("qwertyuiop")
            second = set("asdfghjkl")
            third = set("zxcvbnm")
            possible = 3

            for ch in word:
                if ch.lower() not in first:
                    possible -= 1
                    break
            for ch in word:
                if ch.lower() not in second:
                    possible -= 1
                    break
            for ch in word:
                if ch.lower() not in third:
                    possible -= 1
                    break
            
            if possible > 0:
                ans.append(word)

        return ans