class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = 'aeiouAEIOU'
        half_len = len(s)//2
        count1 = 0
        count2 = 0
        
        for i in range(half_len):
            if s[:half_len][i] in vowels:
                count1 += 1
            if s[half_len:][i] in vowels:
                count2 += 1
        
        return count1 == count2