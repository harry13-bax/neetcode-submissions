class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for i in range (len(nums)):
            res=target-nums[i]
            if res in di:
                return [di[res],i]
            di[nums[i]]=i

        