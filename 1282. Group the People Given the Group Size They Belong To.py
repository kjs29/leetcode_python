class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        fr = {}
        for i in range(len(groupSizes)):
            num = groupSizes[i]
            if num not in fr:
                fr[num] = [i]
            else:
                fr[num].append(i)
        
        ans = []
        for k,v in fr.items():
            for i in range(0,len(v),k):                
                ans.append(v[i:i+k])

        return ans