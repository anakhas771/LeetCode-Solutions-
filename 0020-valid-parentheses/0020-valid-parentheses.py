class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closed ={ 
                  ']':'[',
                  ')':'(',
                  '}':'{'  
                }
        for ch in s:
            if ch not in closed:
                stack.append(ch)
            else:
                if  not stack or stack[-1] != closed[ch]:
                    return False
                stack.pop()
        return not stack