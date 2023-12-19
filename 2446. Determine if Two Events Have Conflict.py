class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        def convert(string):
            return int(string[0]+string[1]+string[3]+string[4])
        
        if convert(event1[0]) > convert(event2[1]) or convert(event2[0]) > convert(event1[1]):
            return False
            
        return True