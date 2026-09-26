class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}": "{", "]": "[", ")": "("}
        stack = []

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
                
        return not stack

    # time complexity: O(n), where n is the length of the input string s. We iterate through each character in the string once, performing constant-time operations for each character.
    # space complexity: O(n), where n is the length of the input string s. In the worst case, we may need to store all opening brackets in the stack, which can take up to O(n) space.
