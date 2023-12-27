class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        max_nums = []
        for num in nums:
            max_nums.append(max(str(num)))

        ans = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                first = max_nums[i]
                second = max_nums[j]
                if first == second:
                    ans = max(ans, (nums[i]+nums[j]))
        
        return ans