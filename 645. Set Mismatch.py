class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # set dictionary that counts each number's frequencies
        fr = {}
        for num in nums:
            if num not in fr:
                fr[num] = 1
            else:
                fr[num] += 1

        # append the duplicated number
        ans = []
        for num, count in fr.items():
            if count == 2:
                ans.append(num)
                break

        # append the missing number
        for n in range(1, len(nums)+1):
            if n not in fr:
                ans.append(n)
                return ans