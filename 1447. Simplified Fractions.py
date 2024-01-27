class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            m = min(a,b)
            for i in range(m, 0, -1):
                if a % i == 0 and b % i == 0:
                    return i
            return 1
        
        ans = []
        for den in range(n,1,-1):
            for nom in range(den,0,-1):
                if gcd(den,nom) == 1:
                    ans.append(f"{nom}/{den}")
        
        return ans