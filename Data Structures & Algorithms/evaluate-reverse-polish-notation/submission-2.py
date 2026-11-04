class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # IDEA: popleft from stack, keep doing that saving the at max two numbers ( i believe this is the rule)
        

        #NEW IDEA, create a stack, push everything from tokens lst
        # once hit a operator pop top two of the stack and do the math. then push the result to stack. repeat till
        # stack is empty, if stack not empty idk doesnt work lol

        stack = []

        for token in tokens:
            
            
            if token == "+": # check first if token is operator if not it's a number
                sVal = stack.pop() # 2
                fVal = stack.pop() # 1 
                total = fVal + sVal
                stack.append(total)

            elif token == "-":
                sVal = stack.pop() # 2
                fVal = stack.pop() # 1 
                total = fVal - sVal
                stack.append(total)               
            elif token == "*":
                sVal = stack.pop() # 2
                fVal = stack.pop() # 1 
                total = fVal * sVal
                stack.append(total)            
            elif token == "/":
                sVal = stack.pop() # 2
                fVal = stack.pop() # 1 
                total = int(fVal / sVal)
                stack.append(total)

            else: # case for number
                stack.append(int(token))

        return stack.pop()
            








            # third case it's not either nvm this is in constarints