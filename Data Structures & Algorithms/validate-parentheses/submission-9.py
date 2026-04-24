class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack 
        # pop top open parenthesis, if parenthesis open then next one can only
        # be another open or the poped opposite parenthesis

        stack = []
        
        correspond = {"(" : ")", "{" : "}", "[" : "]"}
        for char in s:
            if char in correspond:
                stack.append(char)
            else: # right parenthesis
                if((len(stack)) == 0 or (correspond[stack.pop()] != char)):
                    return False
        return len(stack) == 0