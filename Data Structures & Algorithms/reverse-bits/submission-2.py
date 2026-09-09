class Solution:
    def reverseBits(self, n: int) -> int:

        lis = []
        while n > 0:
            remainder = n % 2
            lis.append(remainder)
            n = n // 2
        while len(lis) < 32:
            lis.append(0)
        res = 0
        power = 31

        for bit in lis:
            res += bit * (2 ** power)
            power -= 1
        return res