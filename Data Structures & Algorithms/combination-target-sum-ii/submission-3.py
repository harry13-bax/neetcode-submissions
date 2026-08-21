class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        pes = []

        def backtrack(i, total):
            if total == target:
                res.append(pes.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # Take
            pes.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            pes.pop()

            # Skip all duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Skip
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res