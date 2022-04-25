class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        total = []
        x = []
        
        for i in s:
            if i != ' ':
                x.append(i)
            else:
                total.append(x)
                x = []
                        
        if x:
            total.append(x)

        total.reverse()

        for i in total:
            if i:
                return len(i)
    
