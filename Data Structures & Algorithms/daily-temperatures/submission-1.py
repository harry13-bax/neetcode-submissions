class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[]
        for i in range (len(temperatures)):
            count=0
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    count=j-i
                    break
            stack.append(count)
        return stack


        