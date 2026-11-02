class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temps in enumerate(temperatures):
            while stack and temps > temperatures[stack[-1]]:
                previous_day = stack.pop()
                result[previous_day] = index - previous_day

            stack.append(index)
        
        return result