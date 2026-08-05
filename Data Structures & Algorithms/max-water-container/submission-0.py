class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        max=0
        right=(len(heights)-1)
        while left<right:
            width=right-left
            area=width*(min(heights[right],heights[left]))
            if area>max:
                max=area
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return max


        