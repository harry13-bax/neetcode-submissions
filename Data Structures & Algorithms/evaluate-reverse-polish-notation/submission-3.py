class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range (len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int((tokens[i])))
            if tokens[i]=='+':
                b=(stack.pop())
                a=(stack.pop())
                res=a+b
                stack.append(res)
            elif tokens[i]=='/':
                b=stack.pop()
                a=stack.pop()
                res=int(a/b)
                stack.append(res)
            elif tokens[i]=='-':
                b=stack.pop()
                a=stack.pop()
                res=a-b
                stack.append(res)
            elif tokens[i]=='*':
                b=stack.pop()
                a=stack.pop()
                res=a*b
                stack.append(res)
        return stack[-1]
            

