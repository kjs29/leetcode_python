class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        ans = 0
        undecided = 0
        for ch in moves:
            if ch == "L":
                ans -= 1
            elif ch == "R":
                ans += 1
            else:
                undecided += 1
        
        return abs(ans) + undecided