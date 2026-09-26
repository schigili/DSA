class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {k: v for k, v in knowledge}
        res = []
        curr = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                res.append(d.get("".join(curr), "?"))
                curr.clear()
            elif in_bracket:
                curr.append(char)
            else:
                res.append(char)
                
        return "".join(res)