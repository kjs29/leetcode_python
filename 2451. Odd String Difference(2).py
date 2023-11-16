class Solution:
    def oddString(self, words: List[str]) -> str:
        d = {}    # will contain odd string
        
        for word in words:
            tmp = []     # will contain difference integer array
            for i in range(1,len(word)):
                diff = ord(word[i])-ord(word[i-1])
                tmp.append(diff)
            
            # delete existing key:value pair so that only the string which appears once remains
            pattern = tuple(tmp)
            if pattern not in d:
                d[pattern] = word
            else:
                del d[pattern]
        
        return list(d.values())[0]
    
# Another soluton
class Solution:
    def oddString(self, words: List[str]) -> str:
        
        diffs = []  # will contain difference integer array
        for word in words:
            tmp = []
            for i in range(1, len(word)):
                tmp.append(ord(word[i]) - ord(word[i-1]))
            diffs.append(tmp)
        
        seen = {}   # { difference integer array : [ frequency, index position ] }
        for i in range(len(diffs)):
            pattern = tuple(diffs[i])
            if pattern not in seen:
                seen[pattern] = [1,i]
            else:
                seen[pattern][0] += 1
        
        for k,v in seen.items():
            if v[0] == 1:   # if appears only once
                return words[v[1]]
