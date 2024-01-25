class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_seen = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            num = nums[i]
            if num <= max_seen:
                ans += (max_seen + 1 - num)
                max_seen += 1
            else:
                max_seen = num

        return ans