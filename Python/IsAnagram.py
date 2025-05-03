class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #ch_set = {}
        array_26_zeros = [0 for _ in range(26)]
        for i in s:
            k = ord(i)-ord('a')
            array_26_zeros[k] = array_26_zeros[k]+1
        for i in t:
            k = ord(i)-ord('a')
            array_26_zeros[k] = array_26_zeros[k]-1
        for i in array_26_zeros:
            if i!=0:
                return False
        return True


        
