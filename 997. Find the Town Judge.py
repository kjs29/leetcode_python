class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        mapping = {} # {person: [how_many_people_votes_for_this_person, did_this_person_vote]}
        
        for i in range(1,n+1):
            mapping[i] = [0, False]
        for fr,to in trust:
            mapping[fr][1] = True
            mapping[to][0] += 1
        
        for candidate, val in mapping.items():
            if val[0] == n - 1 and val[1] == False:
                return candidate
        
        return -1

# Another solution
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        count_votes = [0] * n   # each number represents the number of votes (i+1)th person receives
        did_vote = [False] * n  # True means (i+1)th person voted, False means not voted
        
        for fr,to in trust:
            did_vote[fr-1] = True
            count_votes[to-1] += 1

        for i in range(n):            
            if count_votes[i] == n-1 and did_vote[i] == False:
                return i+1
        
        return -1
