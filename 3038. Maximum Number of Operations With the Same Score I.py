class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        prevSum = nums[0] + nums[1]
        ans = 1
        for i in range(2, len(nums) - 1, 2):
            curSum = nums[i] + nums[i + 1]
            if prevSum == curSum:
                ans += 1
            else:
                break
        return ans