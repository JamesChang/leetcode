class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        
        nums = list(str(i) for i in range(1, n+1))
        result = self.getPermutation2(n,k,nums)
        return "".join(result)
    
    def getPermutation2(self, n, k, nums):
        
        if n == 1:
            return nums
        
        def factorial(n):
            if n == 1: 
                return 1
            else:
                return n * factorial(n-1)
                
        n_1_fac = factorial(n-1)
        base = ((k-1) // n_1_fac) 
        plus_k = k - base * n_1_fac
        
        pick = nums[base]
        nums_new = nums[:]
        nums_new.remove(pick)
        
        next_picks = self.getPermutation2(n-1, plus_k, nums_new)
        
        return [pick] + next_picks
        