class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sem=set()
        count=1
        maxi=1
        if nums==[]:
            return 0
        for i in range(len(nums)):
            sem.add(nums[i])
        lst=list(sem)
        lst.sort()
        for i in range (len(lst)-1):
            if lst[i]+1==lst[i+1]:
                count+=1
                if count>maxi:
                    maxi=count
            else:
                count=1
        return maxi
            

        