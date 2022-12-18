def count_primes(n):
    ans = []
     
    while n % 2 == 0:
        ans.append(2)
        n = n // 2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            ans.append(i)
            n = n // i
             
    if n > 2: ans.append(n)
    return ans
        
    
class Solution:
    
    def smallestValue(self, n: int) -> int:
        if n == 4: return 4
        primes = count_primes(n)
        print(primes)
        while len(primes)  != 1:
            s = sum(primes)
            primes = count_primes(s)
            
        return primes[0]