class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0 for _ in range(len(boxes))]
        
        for i in range(len(boxes)):
            tmp = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == "1":
                    tmp += abs(j - i)
            ans[i] = tmp
        
        return ans