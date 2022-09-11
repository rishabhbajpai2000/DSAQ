class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i%2 == 0:
                if freq.__contains__(i):
                    freq[i]+= 1
                else:
                    freq[i] = 1
                    
        if len(freq) == 0: return -1
        
        m_freq_elem = 0
        m_freq = 0
        for i in freq:
            if freq[i]>m_freq:
                m_freq = freq[i]
                m_freq_elem = i
                
            if freq[i] == m_freq and i<m_freq_elem: m_freq_elem = i
        return m_freq_elem