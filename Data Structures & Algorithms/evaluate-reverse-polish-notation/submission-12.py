class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # when encounter with sign, always pops out last two elements
        nums = []
        for t in tokens:
            if t in "+-*/":
                num1 = nums.pop()
                num2 = nums.pop()
                if t == "+":
                    nums.append(num2+num1)
                elif t == "-":
                    nums.append(num2-num1)
                elif t == "*":
                    nums.append(num2*num1)
                elif t == "/":
                    nums.append(int(num2/num1))
            else:
                nums.append(int(t))            
        return nums[0]
        