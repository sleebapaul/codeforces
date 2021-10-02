"""
Leetcode 187. Repeated DNA Sequences

The idea is to keep a sliding window with length 10 and keep the patterns in hashmap

"""

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 10:
            return []
        
        result = set()
        lookup = set()
        tmp = ""
        
        for window_end in range(len(s)):
            tmp += s[window_end]
            
            if len(tmp) == 10:
                
                if tmp in lookup:
                    if tmp not in result:
                        result.add(tmp)
                else:
                    lookup.add(tmp)
                
                tmp = tmp[1:]
                
        return list(result)