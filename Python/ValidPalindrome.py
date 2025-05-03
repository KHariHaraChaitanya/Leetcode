import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Len=0
        st = str()
        for i in s:
            if i.isalnum():
                st = st+i
        
        st = st.lower()
        Len = len(st)
        print(Len)
        print(st)
        for i in range(len(st)//2):
            if st[i] != st[-i-1]:
                return False
        return True

