class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c == '*':
                operator_2 = stack.pop()
                operator_1 = stack.pop()
                result = operator_1 * operator_2
                stack.append(result)
            elif c == '/':
                operator_2 = stack.pop()
                operator_1 = stack.pop()
                result = int(operator_1 / operator_2)
                stack.append(result)
            elif c == '+':
                operator_2 = stack.pop()
                operator_1 = stack.pop()
                result = operator_1 + operator_2
                stack.append(result)
            elif c == '-':
                operator_2 = stack.pop()
                operator_1 = stack.pop()
                result = operator_1 - operator_2
                stack.append(result)
            else:
                stack.append(int(c))
        return stack[0]


solution = Solution()
tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(solution.evalRPN(tokens))