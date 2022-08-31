#tc : O(n)
#sc : O(1)
class Solution:
    def findDisappearedNumbers(self, nums):
        if len(nums) <= 1: return []
        n = len(nums)
        res = []
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
            else:
                nums[i] *= -1
        return res        
        

    
#         result = []
#         nums.sort()
#         print(nums)
#         i = 0
#         j = 1
#         while(i<len(nums)):
#             if nums[i] != j:
#                 result.append(j)
#                 # print(result)
#                 j += 1
                
#             else:
#                 while(nums[i]==j):
#                     # print(nums[i])
#                     i += 1
#                     if(i == len(nums)):
#                         break
#                 j += 1
                
#         while(j <= len(nums)):
#             result.append(j)
#             j += 1
        
#         return result
                
        
obj = Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))