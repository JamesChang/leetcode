class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        
        n = len(nums)
        picks = nums[:]
        masks = list(0 for i in nums)
        nums.sort()
        results = []
        
        def dfs(phase, last=None):

            if phase == n:
                results.append(list(picks))
                return
            
            i=0
            for i in range(n):
                if masks[i] ==0:
                    num = nums[i]
                    
                    if num == last:
                        continue

                    masks[i] = 1
                    picks[phase] = num
                    
                    phase_end = phase +1
                    j = i + 1
                    while j< n and nums[j] == num and masks[j] == 0:
                        picks[phase_end] = num
                        masks[j] = 1
                        j+=1
                        phase_end +=1
                    
                    
                    dfs(phase_end, num)

                    j -= 1
                    while j>=0 and j>=i:
                        masks[j] = 0
                        j -= 1
                    
                    
        dfs(0)
        return results
