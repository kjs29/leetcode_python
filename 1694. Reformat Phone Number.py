class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = ""
        for each in number:
            if each.isdigit():
                nums += each
        
        ans = []
        for i in range(0,len(nums),3):
            if len(nums) - i <= 4:
                if len(nums) - i == 4:
                    ans.append(nums[i:i+2])
                    ans.append(nums[i+2:])
                elif len(nums) - i == 3 or len(nums) - i == 2:
                    ans.append(nums[i:])
                break
            else:
                ans.append(nums[i:i+3])
        
        return "-".join(ans)