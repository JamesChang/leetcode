class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        
        def _restoreIpAddresses(s, phase):
            
            if phase == 0:
                if s == "":
                    return []
                else:
                    return None
            
            if len(s) > phase*3 or len(s) < phase:
                return []
                
                
            result = []
                
            for i in range(1, 4):
                if len(s) >= i:
                    try:
                        v = int(s[:i])
                        if v >255:
                            break
                        if len(str(v)) != i:
                            continue
                    except ValueError:
                        continue
                    
                    next = _restoreIpAddresses(s[i:], phase-1)
                    if phase == 1:
                        if next != []:
                            continue
                        result.append([str(v)])
                    else:
                        if not next:
                          continue

                        for n in next:
                            result.append([str(v)] + n)
                        
            return result
            
        sub_results = _restoreIpAddresses(s,4)
        return [ ".".join(sub_result) for sub_result in sub_results]
            