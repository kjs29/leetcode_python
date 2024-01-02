class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        if len(set(nums)) == len(nums):
            return [nums]
        
        fr = {}
        for num in nums:
            if num not in fr:
                fr[num] = 1
            else:
                fr[num] += 1
        
        ans = []
        while True:
            tmp = []
            all_zero = True
            for k,v in fr.items():
                if v > 0:
                    tmp.append(k)
                    fr[k] -= 1
                    all_zero = False
            ans.append(tmp)
            if all_zero:
                break
        ans.pop()
        
        return ans