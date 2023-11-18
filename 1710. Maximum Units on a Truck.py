class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # sort based on the second element of nested array, in decreasing order
        boxTypes.sort(key=lambda x: x[1], reverse=True) 
        
        total_unit = 0
        for box, unit in boxTypes:
            if truckSize >= box:
                total_unit += (unit * box)
                truckSize -= box
            else:
                total_unit += (truckSize * unit)
                break
        
        return total_unit