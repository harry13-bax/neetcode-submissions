class Solution:
    def countBits(self, n: int) -> List[int]:

        mannu = []

        for i in range(n + 1):

            temp = i
            count = 0

            while temp > 0:
                result = temp % 2

                if result == 1:
                    count += 1

                temp = temp // 2

            mannu.append(count)

        return mannu