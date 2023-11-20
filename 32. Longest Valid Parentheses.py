class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        valid = [False for _ in range(len(s))]  # track valid parentheses pair 
        stack = [] # keep track of opening parentheses
        
        # first operation: identify valid parentheses
        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                stack.append(i)
            else:
                if stack:
                    last = stack.pop()
                    valid[last] = True
                    valid[i] = True

        # second operation: find out the maximum length of consecutive valid parentheses
        ans = 0
        consecutive = 0
        for is_valid in valid:
            if is_valid == True:
                consecutive += 1
                ans = max(consecutive, ans)
            else:
                consecutive = 0
            
        return ans