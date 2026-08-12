class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lis=[]
        for i in matrix:
            lis.extend(i)
        left=0
        right=len(lis)-1
        while left<=right:
            mid=(left+right)//2
            if target==lis[mid]:
                return True
            if target>lis[mid]:
                left=mid+1
            if target<lis[mid]:
                right=mid-1
        return False