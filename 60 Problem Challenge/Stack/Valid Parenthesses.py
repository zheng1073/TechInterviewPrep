"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
def isValid(self, s: str) -> bool:
        if len(s) == 1: 
            return False
        openChar = ['(','[','{']
        closeChar = [')',']','}']
        stack = []
        
        for char in s:
            if char in openChar:
                stack.append(char)
            if char in closeChar:
                try:
                    lastValue = stack[-1]
                except:
                    return False
                if (openChar.index(lastValue) == closeChar.index(char)):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
"""
Runtime: 18 ms, faster than 99.14% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 64.46% of Python3 online submissions for Valid Parentheses.
"""
