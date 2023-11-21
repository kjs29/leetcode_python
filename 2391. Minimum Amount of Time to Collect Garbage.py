class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        total_travel = 0
        
        # how far each truck has to go 
        metal, paper, glass = 0, 0, 0
        for i in range(len(garbage)):
            house = garbage[i]
            if "M" in set(house):
                metal = i
            if "P" in set(house):
                paper = i
            if "G" in set(house):
                glass = i

        # calculate travel time for each truck, and add to total
        for i in range(len(travel)):
            if metal != 0 and i + 1 <= metal:
                total_travel += travel[i]
            if paper != 0 and i + 1 <= paper:
                total_travel += travel[i]
            if glass != 0 and i + 1 <= glass:
                total_travel += travel[i]
        
        # calculate total pick up time
        total_pickup = len("".join(garbage))
        
        return total_travel + total_pickup