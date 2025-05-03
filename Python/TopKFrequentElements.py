class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}   # num - freq map 
        freqz = [[]for i in range(len(nums)+1)]  
        # 
        for n in nums:
            count[n] =  count.get(n,0)+1
        for n,c in count.items():
            freqz[c].append(n)
        res = []

        for i in range(len(freqz)-1, 0, -1):
            for n in freqz[i]:
                res.append(n)
                if len(res)==k:
                    return res
        


        
        
