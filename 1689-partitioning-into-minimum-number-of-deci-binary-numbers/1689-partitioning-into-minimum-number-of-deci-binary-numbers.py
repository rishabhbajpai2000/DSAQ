class Solution:
    def minPartitions(self, n: str) -> int:
        num_int = []
        s = set()
        for i in n:
            s.add(int(i))
        num_int = list(s)
        num_int.sort(reverse=True)
        
        count = 0
        while True:
            if len(num_int) ==1:
                count += num_int[0]
                break
                
            count += num_int[-1]
            
            for i in range(len(num_int)):
                num_int[i] -= num_int[-1]

            num_int.pop()
    
        return count
            
        