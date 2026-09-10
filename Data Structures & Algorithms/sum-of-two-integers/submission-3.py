class Solution:
    def getSum(self, a: int, b: int) -> int:
        pes=1
        res=0
        har=0xFFFFFFFF
        while pes>0:
            res=(a^b)&har
            pes=((a&b)<<1)&har
            a=res
            b=pes
        if res > 0x7FFFFFFF:
            res -= 0x100000000
        return res

        