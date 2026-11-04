class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)

        stack = [] # one that one hold [temp, index]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackI = stack.pop()
                results[stackI] = (index - stackI) # r - l



            stack.append([temp, index])

        return results