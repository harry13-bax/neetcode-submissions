class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        lis=[]
        while left<=len(nums)-k:
            maxi=float('-inf')
            for i in range(left,left+k):
                if nums[i]>maxi:
                    maxi=nums[i]
            lis.append(maxi)
            left+=1
        return lis


        