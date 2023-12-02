class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def generate(curr_sum,curr,index):
            
            if curr_sum == target:
                ans.append(curr)
                return
            
            for i in range(index, len(candidates)):
                n = candidates[i]
                if curr_sum > target:
                    break
                if curr_sum < target:
                    generate(curr_sum+n,curr+[n],i)

        ans = []
        curr = []
        generate(0,curr,0)
        
        return ans