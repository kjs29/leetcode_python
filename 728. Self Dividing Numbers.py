class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_sdn(n):
            for number in str(n):
                if number == "0" or n % int(number) != 0:
                    return False
            return True
        
        ans = []
        for num in range(left, right+1):
            if is_sdn(num):
                ans.append(num)
        
        return ans