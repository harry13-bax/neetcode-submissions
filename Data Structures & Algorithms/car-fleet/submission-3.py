class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(reverse=True)
        count=0
        prevt=0
        for p,s in cars:
            time=(target-p)/s
            if time>prevt:
                count+=1
                prevt=time

                
        return count

        