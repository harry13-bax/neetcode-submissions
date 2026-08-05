class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        siu = {}
        for i in nums:
            if i in siu:
                siu[i] += 1
            else:
                siu[i] = 1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in siu.items():
            freq[count].append(num)
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        