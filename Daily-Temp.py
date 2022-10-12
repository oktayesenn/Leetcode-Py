# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# temperatures = [73,74,75,71,69,72,76,73]
# def solution():
    
#     result = [0] * len(temperatures)
#     myStack = []

#     for ix, tempature in enumerate(temperatures):
#         while myStack and tempature > myStack[-1][0]:
#             stackTemp, stackIndex = myStack.pop()
#             result[stackIndex] = ix - stackIndex
#         myStack.append([tempature, ix])
#     return result
# solution()

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
# '''



# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# temperatures = [73,74,75,71,69,72,76,73]



# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         result = [0] * len(temperatures) # initialize with 0s so we don't have to manually add 0s if none is compliant later on
#         myStack = [] #storing pair of temperature and corresponding index 
        
#         for ix, temperature in enumerate(temperatures):
#             while myStack and temperature > myStack[-1][0]:
#                 stackTemperature, stackIndex = myStack.pop()
#                 result[stackIndex] = (ix - stackIndex)
#             myStack.append([temperature, ix])
#         return result
