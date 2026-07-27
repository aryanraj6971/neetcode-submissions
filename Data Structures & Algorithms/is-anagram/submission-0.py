class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def isAnagram(s,t):
            d=sorted(s)
            m=sorted(t)
            if(d==m):
                return True
            else:
                return False
        return(isAnagram(s,t))