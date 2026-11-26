class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        stack = []

        for i in range(len(position)):
            car.append([position[i],speed[i]])
        
        car.sort(reverse=True)

        for i in range(len(car)):
            time = (target - car[i][0])/car[i][1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
            
        return len(stack)




        
