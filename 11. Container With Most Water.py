class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0                   # start index of the container
        e = len(height) - 1     # end index of the container
        max_area = 0            # max area to be updated

        while s < e:
            tmp_w = e - s                      # width of current container
            tmp_h = min(height[s],height[e])   # height of current container
            tmp_area = tmp_w * tmp_h           # area of current container
            max_area = max(max_area, tmp_area)
            
            if height[s] < height[e]:       # increase start index if left pillar is smaller
                s += 1
            elif height[e] < height[s]:     # decrease end index if right pillar is smaller
                e -= 1
            else:                           # if they are the same pillar, move both inwards
                s += 1
                e -= 1
        return max_area