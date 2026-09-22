class Solution:
    def isValid(self, s: str) -> bool:
        char = {"}": "{", "]": "[", ")": "("}
        stack = []

        for p in s:
            if not stack or p != char:
                return False
            else:
                stack.append(p)
        
        return not stack
