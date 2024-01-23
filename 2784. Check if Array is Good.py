class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_num = max(nums)
        ans = [n for n in range(1, max_num)] + [max_num] + [max_num]
        
        if len(ans) != len(nums): 
            return False
        return ans == sorted(nums)