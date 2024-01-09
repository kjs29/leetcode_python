class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sum_digits(number):
            ans = 0
            for ch in str(number):
                ans += int(ch)
            return ans
        
        if sum_digits(n) <= target:
            return 0
        
        # Calculate the difference to the next higher round number
        # For example, if n is 467, number = 1000 - 467 = 533
        number = 10**(len(str(n))) - n
        
        for i in range(len(str(number))-1, -1, -1):
            
            # Get the complementary part of the number to reach the next round number
            # For example, if number is 533, comp will be 3, then 33, and finally 533
            comp = int(str(number)[i:])
            
            if sum_digits(n + comp) <= target:
                return comp