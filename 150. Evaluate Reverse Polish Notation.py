class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        notation = "+-*/"
        stack = []
        for token in tokens:
            if token not in notation:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first+second)
                elif token == "-":
                    stack.append(first-second)
                elif token == "*":
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
        
        return stack[0]