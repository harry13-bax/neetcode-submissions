class MinStack:

    def __init__(self):
        self.k=[]
        

    def push(self, val: int) -> None:
        self.k.append(val)
        
        

    def pop(self) -> None:
        self.k.pop()
        

    def top(self) -> int:
        return self.k[-1]
        

    def getMin(self) -> int:
        return min(self.k)
        
