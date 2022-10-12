# Example 1:

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

# class Solution:
#     def calPoints(self, ops: List[str]) -> int:
        
#         # This is O(N) since we are iterating through
#         # Since we are using lifo, stack is great but we can implement it with list as in this example
        
#         stack = []
        
#         for op in ops:
#             if op == "+":
#                 stack.append(stack[-1] + stack[-2])
#             elif op == "C":
#                 stack.pop()
#             elif op == "D":
#                 stack.append(2 * stack[-1])
#             else:
#                 stack.append(int(op))
        
#         return sum(stack)