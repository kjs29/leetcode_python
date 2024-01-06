class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(arr):
            tmp = []
            for i in range(len(arr)):
                if arr[i].isalpha():
                    tmp.append(arr[i])
                elif arr[i] == "#" and tmp:
                    tmp.pop()
            return tmp
        
        return helper(s) == helper(t)