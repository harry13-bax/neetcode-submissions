class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)

        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]

        for i in range(1, n):

            currmax = max(nums[i], nums[i] * maxi, nums[i] * mini)
            currmin = min(nums[i], nums[i] * maxi, nums[i] * mini)

            maxi = currmax
            mini = currmin

            ans = max(ans, maxi)

        return ans