class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        siu=set()
        for num in nums:
            if num in siu:
                return True
            siu.add(num)
        return False