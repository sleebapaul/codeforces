"""
1768. Merge Strings Alternately

Two pointers. Watch the length limit
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        first = True
        second = True
        result = ""
        idx = 0
        
        while first or second :

            if idx < len(word1):
                result += word1[idx]
            else:
                first = False
            if idx < len(word2):
                result += word2[idx]
            else:
                second = False 

            idx += 1

        return result 