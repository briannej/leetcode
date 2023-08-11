class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ']':'[', ')':'('}
        for letter in s:
            if letter in mapping:
                if not stack or stack.pop() != mapping[letter]:
                    return False
            else:
                stack.append(letter)
        if not stack:
            return True