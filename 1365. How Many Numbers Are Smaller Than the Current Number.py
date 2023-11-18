class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mapping = {}
        sorted_nums = sorted(nums)  # sort list
        
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in mapping:   
                                                
                mapping[sorted_nums[i]] = i     # The Index of the first number's occurence is of 
                                                # the count smaller numbers than it.
        ans = []
        for i in range(len(nums)):
            ans.append(mapping[nums[i]])
        
        return ans