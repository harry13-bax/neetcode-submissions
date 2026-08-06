class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        maxi = 0          
        dic = {}
        ans = 0

        for right in range(len(s)):

            
            if s[right] in dic:
                dic[s[right]] += 1
            else:
                dic[s[right]] = 1

            
            maxi = max(maxi, dic[s[right]])

            
            
            while (right - left + 1) - maxi > k:
                dic[s[left]] -= 1
                left += 1

        
            ans = max(ans, right - left + 1)

        return ans
                







        

