class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        pes = []

        def backtrack(i, total):
            if total == target:
                res.append(pes.copy())
                return

            if total > target or i >= len(nums):
                return

            pes.append(nums[i])
            backtrack(i, total + nums[i])

            pes.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)

        return res