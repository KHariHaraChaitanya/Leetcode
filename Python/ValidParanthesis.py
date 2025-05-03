class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = set(["(","[","{"])
        #cl = set(')',']','}')
        for i in s:
            if i in op:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ')' and stack[-1]=='(':
                    stack.pop()
                elif i == ']' and stack[-1]=='[':
                    stack.pop()
                elif i == '}' and stack[-1]=='{':
                    stack.pop()
                else :
                    return False
        return len(stack) == 0

                

        
        
