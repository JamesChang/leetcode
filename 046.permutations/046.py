class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        
        n = len(nums)
        picks = nums[:]
        masks = list(0 for i in nums)
        results = []
        
        def dfs(phase):
            
            for i, num in enumerate(nums):
                if masks[i] ==0:
                    picks[phase] = num
                    
                    if phase == n-1:
                        results.append(list(picks))
                    
                    masks[i] = 1
                    dfs(phase+1)
                    masks[i] = 0
                    
                    
        dfs(0)
        return results
                    
                    