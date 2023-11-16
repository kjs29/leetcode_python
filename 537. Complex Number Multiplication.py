class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
    
        r_1 = int(num1[0])
        i_1 = int(num1[1].replace("i",""))
        r_2 = int(num2[0])
        i_2 = int(num2[1].replace("i",""))
        
        r = str((r_1 * r_2) - (i_1 * i_2))  # subtract since i^2 = -1
        i = str((i_1 * r_2) + (i_2 * r_1)) + "i"
        return r + "+" + i