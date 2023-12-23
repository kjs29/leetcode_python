class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        trace = {tuple([0,0]):1} # or, set([(0,0)])
        curr_coor = [0,0]
        
        for each in path:
            if each == "N":
                curr_coor[0]-=1
            elif each == "S":
                curr_coor[0]+=1
            elif each == "W":
                curr_coor[1]-=1
            elif each == "E":
                curr_coor[1]+=1
            
            if tuple(curr_coor) in trace:
                return True
            
            trace[tuple(curr_coor)] = 1
        
        return False