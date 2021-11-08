"""
165. Compare Version Numbers

Straight forward. Use two ptrs or make the length of arrays be same and use a single pointer

Time: O(N)
Space: O(N)
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        ver_one_list = version1.split(".") # ["1", "01"]
        ver_two_list = version2.split(".") # ["1", "001"]
        
        max_len = max(len(ver_one_list), len(ver_two_list))
        
        for _ in range(max_len):
            
            if len(ver_one_list) < max_len:
                ver_one_list.append("0")
            
            if len(ver_two_list) < max_len:
                ver_two_list.append("0")

        ptr = 0
        
        while ptr < len(ver_one_list) : # 0 < 2, 0 < 2
             
            a = ver_one_list[ptr] # 1 
            b = ver_two_list[ptr] # 1 
                        
            if int(a) > int(b):
                return 1
            
            elif int(a) < int(b):
                return -1
            
            ptr += 1

        return 0 