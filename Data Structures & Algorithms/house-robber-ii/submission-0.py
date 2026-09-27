class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp = [0]*(n + 2)
        for i in range(n-1,0,-1):
            dp[i]=max(nums[i]+dp[i+2],dp[i+1])
        pp = [0]*(n + 2)
        for i in range(n-2,-1,-1):
            pp[i]=max(nums[i]+pp[i+2],pp[i+1])
        return max(pp[0],dp[1])



        