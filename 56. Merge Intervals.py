class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        ans = [intervals[0]]
        
        for i in range(1, len(intervals)):
            prev_first = ans[-1][0]
            prev_second = ans[-1][1]
            curr_first = intervals[i][0]
            curr_second = intervals[i][1]
            
            if curr_first > prev_second:
                ans.append([curr_first, curr_second])
            else:
                ans[-1][1] = max(prev_second, curr_second)
        
        return ans