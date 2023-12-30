class Solution:
    def arrangeWords(self, text: str) -> str:
        
        seen = {}
        text = text.split(" ")
        for word in text:
            if len(word) not in seen:
                seen[len(word)] = [word.lower()]
            else:
                seen[len(word)].append(word.lower())
        
        ans = []
        for v in seen.values():
            ans += v
        
        return " ".join(sorted(ans, key=len)).capitalize()