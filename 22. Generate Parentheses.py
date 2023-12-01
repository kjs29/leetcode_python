class Solution:
    def backtrack(self, n, curr, open, close, ans):
        
        # base case
        if n == open and n == close:
            ans.append(curr)
            return
        
        # two recursive cases
        if open != n:
            self.backtrack(n, curr + "(", open + 1, close, ans)
        
        if open > close:
            self.backtrack(n, curr + ")", open, close + 1, ans)

    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        self.backtrack(n, "(", 1, 0, ans)
        
        return ans