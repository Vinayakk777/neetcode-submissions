class Solution:
    def isValid(self, s: str) -> bool:
        verify={"}":"{",
                ")":"(",
                "]":"["}
        
        stack=[]
        for c in s:
            if c in verify:
                if stack and stack[-1]==verify[c]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False

        