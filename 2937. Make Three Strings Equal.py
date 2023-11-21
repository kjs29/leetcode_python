class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
        if s1 == s2 == s3:
            return 0
        
        shortest = min(len(s1),len(s2),len(s3))
        
        if not (s1[:1]==s2[:1]==s3[:1]):
            return -1
            
        index_remove_from = shortest
        for i in range(shortest):
            if not (s1[i]==s2[i]==s3[i]):
                index_remove_from = i
                break
        
        operation = len(s1[index_remove_from:]) + \
                    len(s2[index_remove_from:]) + \
                    len(s3[index_remove_from:])
        
        return operation