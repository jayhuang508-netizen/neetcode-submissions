class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use another stack to store the days which has hoter one 
        res = []
        temp_stack_index = []
        for i in range(len(temperatures)-1,0,-1):
            if temperatures[i]>temperatures[i-1]:
                temp_stack_index.append(i)
        for j, temp in enumerate(temperatures):
            diff = 0
            for k in reversed(temp_stack_index):
                if temp< temperatures[k] and k>=j:
                    diff = k-j
                    break
            res.append(diff)
        return res
                
        