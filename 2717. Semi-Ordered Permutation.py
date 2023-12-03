class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
        f = nums.index(1)   # 1's index position but it can be number of swaps to make 1 get to 0's position.
        l = nums.index(len(nums))   # last number's index position 

        if f == 0 and l == len(nums) - 1:   # if nums is already semi-ordered
            return 0
        
        # Explanation:
        # [2,4,1,3] => when 1,4 are swapped, 4's position moves one to the right
        if l < f:
            l += 1
        
        return f + (len(nums) - 1 - l)