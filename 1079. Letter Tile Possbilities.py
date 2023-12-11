class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def generate(arr, available, curr):
            if not available:
                return 
            for ch in available:
                ans.append(curr + ch)
                tmp = available.copy()
                tmp.remove(ch)
                generate(arr, tmp, curr + ch)
        
        ans = []
        generate(list(tiles),list(tiles),"")
        
        return len(set(ans))