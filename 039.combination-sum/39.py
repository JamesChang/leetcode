class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        
        self.n = len(candidates)
        self.candidates = candidates
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
        self.pick.append(element)
        self._make(pick, remains - element)
        self.pick.pop()
        self._make(pick +1, remains)