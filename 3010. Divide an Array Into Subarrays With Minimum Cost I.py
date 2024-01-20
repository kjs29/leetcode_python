class Solution:
    def minimumCost(self, nums: List[int]) -> int:
    
        first = nums[0]
        the_other_two = sorted(nums[1:])[:2]
        
        return sum( [first] + the_other_two )