class Solution:
    def isValid(self, s: str) -> bool:
        
        px_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        px_dict_rev = {
            ")":"(" ,
            "]":"[",
            "}":"{"
        }

        stack = []
        flag = True
        for i in s:
            cross = px_dict.get(i)
            if cross:
                stack.append(i)
            else:
                front = stack.pop(-1) if stack else None
                rev = px_dict_rev.get(i)
                if front != rev:
                    flag = False
        if flag and not stack:
            return True
        else:
            return False
