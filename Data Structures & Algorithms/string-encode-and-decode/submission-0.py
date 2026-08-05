class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=''
        for siu in strs:
            ans+=str(len(siu))+'#'+siu
        return ans


    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=s.find('#',i)
            length=int(s[i:j])
            start=j+1
            word=s[start:start+length]
            ans.append(word)
            i=start+length
        return ans


