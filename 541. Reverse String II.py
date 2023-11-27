class Solution:
    def reverseArr(self, arr, idx):
        """
        Reverse subarrays in 'arr' based on 'idx'.
        arr : [1,2,3,4,5,6,7,8,9,10]
        idx : [[0,1,2],[7,8]]
        return : [3,2,1,4,5,6,7,9,8,10]
        """
        for each in idx:
            start = each[0]
            end = each[-1]
            while start < end:
                arr[start],arr[end] = arr[end],arr[start]
                start += 1
                end -= 1
        return arr

    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        ans = []
        i = 0
        while i < len(s):
            rem_ch = len(s) - i
            if rem_ch < k:
                tmp = []
                for n in range(i, len(s)):
                    tmp.append(n)
                ans.append(tmp)
                break
            elif rem_ch >= k:
                tmp = []
                for n in range(i,i+k):
                    tmp.append(n)
                ans.append(tmp)
                i += k * 2
        
        return "".join(self.reverseArr(s,ans))