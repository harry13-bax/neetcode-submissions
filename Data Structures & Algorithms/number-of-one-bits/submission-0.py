class Solution:
    def hammingWeight(self, n: int) -> int:
        result=0
        count=0
        hi=[]
        fi=[]
        while n>0:
            result=n%2
            hi.append(result)
            n=n//2
        fi=hi[::-1]
        for i in fi:
            if i==1:
                count+=1
        return count
