"""
2000. Reverse Prefix of Word

Pretty straight forward. Made an effort to not using reverse function or [::-1] notation.

"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        queue = []
        flag = False
        idx = 0
        
        for i in range(len(word)):
            
            queue.append(word[i])
            
            if word[i] == ch:
                flag = True
                idx = i
                break
        
        if not flag:
            return word
        
        result = ""
        while queue:
            char = queue.pop()
            result += char
        
        return result + word[idx+1:]