class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def generate(string, start, curr):
            if start == len(string):
                ans.append(curr)
                return
            if string[start].isalpha():
                generate(string, start+1, curr+string[start].swapcase())
                generate(string, start+1, curr+string[start])
            else:
                generate(string, start+1, curr+string[start])

        ans = []
        generate(s, 0, "")
        
        return ans