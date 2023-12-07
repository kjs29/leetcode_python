from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        """
        a^2 + b^2 = c
        (a+1)(a-1) + (b+1)(b-1) = c - 2
        """
        half = int(sqrt(c))
        possible = []
        for n in range(half + 1):
            possible.append(n ** 2 - 1)
            if 2 * (n ** 2 - 1) == c - 2:
                return True

        left = 0
        right = len(possible) - 1
        while left < right:
            if possible[left] + possible[right] == c - 2:
                return True
            if possible[left] + possible[right] < c - 2:
                left += 1
            else:
                right -= 1

        return False

# Another solution
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        a^2 + b^2 = c
        b^2 = c - a^2
        b = sqrt(c-a^2)
        """
        
        if c <= 2:
            return True
        
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a ** 2)
            if b == int(b):
                return True
            
        return False