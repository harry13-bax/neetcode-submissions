class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        dict={
            '}':'{',
            ']':'[',
            ')':'('
        }
        for i in s:
            if i in '({[':
                lst.append(i)
            else:
                if not lst:
                    return False
                if lst[-1]!=dict[i]:
                    return False
                lst.pop()
        return not lst
            

            