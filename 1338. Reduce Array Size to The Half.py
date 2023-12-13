class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        fr = {}
        for n in arr:
            if n not in fr:
                fr[n] = 1
            else:
                fr[n] += 1
        
        pairing = []
        for k,v in fr.items():
            pairing.append([k,v])
        
        pairing.sort(key=lambda x: x[1], reverse=True)
        
        ans = [0,0] # total, count
        for _, freq in pairing:
            if ans[0] >= len(arr)/2:
                break
            ans[0] += freq
            ans[1] += 1
        
        return ans[1]