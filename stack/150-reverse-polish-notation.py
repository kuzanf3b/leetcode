class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(token))
        
        return stack.pop()

    # time complexity: O(n), where n is the number of tokens
    # space complexity: O(n), where n is the number of tokens
