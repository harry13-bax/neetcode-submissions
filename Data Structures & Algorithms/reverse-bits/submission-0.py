class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        reversed_binary = binary[::-1]

        res = 0
        w = 31

        for j in reversed_binary:
            res += (2 ** w) * int(j)
            w -= 1

        return res