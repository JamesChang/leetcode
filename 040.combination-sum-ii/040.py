class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        
        self.candidates = candidates
        self.n = len(self.candidates)
        self.candidates.sort()
        self.pick = []
        self.result = []
        
        self._make(0, target)
        return self.result
        
        
    def _make(self, pick, remains):
        
        if remains == 0:
            self.result.append(self.pick[:])
            return
        if remains <0:
            return
        if pick == self.n:
            return
        
        element = self.candidates[pick]
        
        j = pick + 1
        while(j < self.n and self.candidates[j] == element):
            j+=1
        
        for i in range(j - pick):
            self.pick.append(element)
            self._make(j, remains - element * i -element )
            
        for i in xrange(pick, j):    
            self.pick.pop()
            
        self._make(j, remains)
        
        
        
        
        