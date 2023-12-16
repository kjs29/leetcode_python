class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        def recursive(number, power):    
            if 2**power > number:
                return False
            if 2**power == number:
                return True
            return recursive(number, power+1)

        return recursive(n, 0)