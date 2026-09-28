class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        if len(s)==1:
            return 1
        def exp(left,right):
            
            while left>=0 and right<len(s) and s[left]==s[right]:
                nonlocal count
                left-=1
                right+=1
                count+=1
            return left+1,right-1
        for i in range(len(s)):
            left1,right1=exp(i,i)
            left2,right2=exp(i,i+1)
        return count