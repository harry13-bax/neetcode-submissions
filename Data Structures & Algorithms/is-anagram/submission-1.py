class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        siu={}
        for x in s:
            if x in siu:
                siu[x]=siu[x]+1
            else:
                siu[x]=1
        for x in t:
            if x not in siu:
                return False
            siu[x]-=1
        for va in siu.values():
            if va!=0:
                return False
        return True
        
                
        

        