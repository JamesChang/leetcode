class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        
        result = []
        picks = []
        
        def next(phase, target, picked):
            
            if target == 0 and picked == k:
                result.append(picks[:])
                return
            
            if picked >= k:
                return 
            
            if target <0:
                return
            
            if phase > 9:
                return
            
            if target < (k-picked) * phase:
                return
            
            picks.append(phase)
            next(phase+1, target-phase, picked+1)
            picks.pop()
            next(phase+1, target, picked)
                
        next(1, n, 0)    
        return result
            