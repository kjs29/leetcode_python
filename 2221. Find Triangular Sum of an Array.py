class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def generate(arr):
            if len(arr) == 1:
                return arr[0]            
            ans = []
            for i in range(len(arr)-1):
                ans.append((arr[i] + arr[i+1]) % 10)
            
            return generate(ans)

        return generate(nums)