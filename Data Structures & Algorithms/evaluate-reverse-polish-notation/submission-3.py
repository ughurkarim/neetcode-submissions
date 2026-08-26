class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c ==  "+":
                stack.append(stack.pop()+stack.pop())
            elif c == "/":
                number1 = stack.pop()
                number2 = stack.pop()
                stack.append(int(number2/number1))
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "-":
                number1 = stack.pop()
                number2 = stack.pop()
                stack.append(number2-number1)
            else:
                stack.append(int(c))
        
        return stack[0]

            

        