class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1={}
        dic2={}
        left=0
        if len(s1)>len(s2):
            return False
        for c in s1:
            if c in dic1:
                dic1[c]+=1
            else:
                dic1[c]=1
        for i in range (len(s2)):
            if s2[i] in dic2:
                dic2[s2[i]]+=1
            else:
                dic2[s2[i]]=1
            if i-left+1 > len(s1):
                dic2[s2[left]]-=1
                if dic2[s2[left]]==0:
                    del dic2[s2[left]]
                left+=1
            if dic1==dic2:
                return True
        return False
            

            