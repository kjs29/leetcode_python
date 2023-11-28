class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        curr_w_count = blocks[:k].count("W")    # number of W's in the initial window
        ans = curr_w_count                      # minimum number of W's in each window
        
        for i in range(len(blocks)-k):
            first = blocks[i]   # current window's first block
            next = blocks[i+k]  # upcoming window's first block
            if first == "W":
                curr_w_count -= 1
            if next == "W":
                curr_w_count += 1
            ans = min(curr_w_count, ans)

        return ans