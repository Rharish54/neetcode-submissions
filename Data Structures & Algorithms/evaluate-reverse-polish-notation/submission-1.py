import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b), 
        }
        nums = []

        for t in tokens:
            if t in ops:
                b = nums.pop()
                a = nums.pop()
                nums.append(ops[t](a, b))
            else:
                nums.append(int(t))

        return nums[0]