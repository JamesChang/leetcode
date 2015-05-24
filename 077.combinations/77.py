
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        
        self.s = range(1, n+1)
        self.n = n
        self.k = k
        self.pick = list(range(k))
        self.result = []
        self._make(0, 0)
        return self.result
        
    def _make(self, picked, element):
        
        if picked == self.k:
            self.result.append(tuple(self.s[p] for p in self.pick))
            return
            
        if element == self.n:
            return
        
        self.pick[picked] = element
        self._make(picked + 1, element + 1)
        self._make(picked, element + 1)