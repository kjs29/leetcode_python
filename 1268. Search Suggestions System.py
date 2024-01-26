class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:        
        ans = []
        tmp = []
        for i in range(len(searchWord)):
            tmp = []
            for j in range(len(products)):
                if searchWord[:i+1] == products[j][:i+1]:
                    tmp.append(products[j])
            ans.append(sorted(tmp)[:3])
        
        return ans