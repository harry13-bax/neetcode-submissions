class Solution:
    def reverseBits(self, n: int) -> int:

        lis = []

        # Convert n to binary
        while n > 0:
            remainder = n % 2
            lis.append(remainder)
            n = n // 2

        # Add zeros until we have 32 bits
        while len(lis) < 32:
            lis.append(0)

        # lis is currently in reverse order,
        # so it is already the reversed binary!
        
        res = 0
        power = 31

        for bit in lis:
            res += bit * (2 ** power)
            power -= 1

        return res