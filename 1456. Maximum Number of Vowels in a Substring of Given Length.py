class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = "aeiou"
        first_ch = s[0]    # first letter of window
        curr_vowel = 0  # current window's vowel count
        max_vowel = 0   # maximum number of each window's vowel counts

        # intialize curr_vowel, and max_vowel with the first window
        for i in range(k):
            if s[i] in vowels:
                curr_vowel += 1 
                max_vowel += 1

        for i in range(k,len(s)):   # iterate from the next window
            if s[i] in vowels:      # if the current character is a vowel, add 1 to curr_vowel
                curr_vowel += 1
            if first_ch in vowels:     # if the previous window's first character was a vowel, subtract 1
                curr_vowel -= 1
            max_vowel = max(max_vowel, curr_vowel)  # update current window's vowel counts
            first_ch = s[i-k+1]        # update the first character to current window for next iteration
            
        return max_vowel