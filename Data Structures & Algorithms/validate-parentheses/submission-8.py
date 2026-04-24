class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack 
        # pop top open parenthesis, if parenthesis open then next one can only
        # be another open or the poped opposite parenthesis

        stack = []
        check = False
        correspond = {"(" : ")", "{" : "}", "[" : "]"}
        for char in s:
            if char in correspond.keys():
                stack.append(char)
                print(char)
            else: # if right parenthesis
                if len(stack) > 0:
                    if correspond[stack.pop()] == char:
                        check = True
                    else:
                        return False
                else: # edge case for when stack empty and is right parenthesis
                    return False
        if len(stack) != 0:
            check = False
        return check