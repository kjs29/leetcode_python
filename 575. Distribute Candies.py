class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        allowed = len(candyType) // 2   # number of candies she can eat
        
        distinct = set()    # unique set of candies she has
        for candy in candyType:
            distinct.add(candy)
        
        return len(distinct) if len(distinct) < allowed else allowed