class Solution:
    def minFlips(self, target: str) -> int:

        if len(set(target)) == 1:
            return 0
            
        ans = 1
        index = target.index("1")
        prev = target[index]
        for i in range(index+1,len(target)):
            curr = target[i]
            if prev != curr:
                ans += 1
            prev = curr
        
        return ans