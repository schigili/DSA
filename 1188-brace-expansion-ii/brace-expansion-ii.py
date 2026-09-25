class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        processed_expr = []
        for i, char in enumerate(expression):
            processed_expr.append(char)
            if i + 1 < len(expression):
                nxt = expression[i + 1]
                if (char.isalpha() or char == '}') and (nxt.isalpha() or nxt == '{'):
                    processed_expr.append('*')
                    
        expr = "".join(processed_expr)
        
        vals = []
        ops = []
        precedence = {'{': 0, ',': 1, '*': 2}
        
        def apply_operator():
            op = ops.pop()
            right = vals.pop()
            left = vals.pop()
            
            if op == '*':
                vals.append({l + r for l in left for r in right})
            elif op == ',':
                vals.append(left.union(right))
                
        for char in expr:
            if char.isalpha():
                vals.append({char})
            elif char == '{':
                ops.append(char)
            elif char == '}':
                while ops and ops[-1] != '{':
                    apply_operator()
                ops.pop() 
            else:
                while ops and precedence[ops[-1]] >= precedence[char]:
                    apply_operator()
                ops.append(char)
                
        while ops:
            apply_operator()
            
        return sorted(list(vals[-1]))