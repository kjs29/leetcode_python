class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        ideal_candy = sum(aliceSizes + bobSizes) // 2
        diff = ideal_candy - sum(aliceSizes)
        bobsCandy = set(bobSizes)
        
        for each in aliceSizes:
            if each + diff in bobsCandy:
                return [each, each + diff]