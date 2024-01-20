class Solution:
    
    def canSortArray(self, nums: List[int]) -> bool:
        
        res = []
        for num in nums:
            res.append([num, bin(num).count("1")])
    
        curr_num = res[0][0]
        curr_bit = res[0][1]
        ans = []
        tmp = [curr_num]
        for num, bit in res[1:]:
            if bit == curr_bit:
                tmp.append(num)
            else:
                for each in sorted(tmp):
                    ans.append(each)
                tmp = [num]
                curr_bit = bit
        
        ans = ans + sorted(tmp)
        
        return all(ans[i] >= ans[i-1] for i in range(1, len(ans)))