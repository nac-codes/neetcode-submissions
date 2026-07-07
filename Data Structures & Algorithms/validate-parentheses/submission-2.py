def isOpen(c: str) -> bool:
    if c in ['(','{','[']:
        return True
    else:
        return False

def reverse(c: str) -> str:
    # set open to closed
    if c == '(':
        return ')'
    if c == '{':
        return '}'
    if c == '[':
        return ']'
    
    return ""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if isOpen(c):
                stack.append(c)
            else:
                if len(stack) < 1 or c != reverse(stack.pop()):
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False