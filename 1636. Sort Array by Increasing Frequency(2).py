class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        fr={}
        for num in nums:
            if num not in fr:
                fr[num] = 1
            else:
                fr[num] += 1
        
        sorted_lst=[]
        for num,freq in fr.items(): 
            appended = False
            for i in range(len(sorted_lst)):
                if freq < sorted_lst[i][1] or (freq == sorted_lst[i][1] and num > sorted_lst[i][0]):
                    sorted_lst.insert(i,(num, freq))
                    appended = True
                    break
            if not appended:
                sorted_lst.append((num, freq))
        
        ans = []
        for num,fr in sorted_lst:
            ans += [num] * fr
        return ans

# Another solution
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        fr={}
        for num in nums:
            fr[num] = fr.get(num, 0) + 1
        
        # sort by x[1], then x[0] but in descending order
        fr_lst=sorted(fr.items(), key=lambda x:(x[1],-x[0]))
        
        ans = []
        for num,fr in fr_lst:
            ans += [num] * fr
        return ans