class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x).replace("0b","")
        y = bin(y).replace("0b","")
        if len(y) > len(x):
            x = "0" * (len(y) - len(x)) + x
        else:
            y = "0" * (len(x) - len(y)) + y
        ans = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                ans += 1
        
        return ans