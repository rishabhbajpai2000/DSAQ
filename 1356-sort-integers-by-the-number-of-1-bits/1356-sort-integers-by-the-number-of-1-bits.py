class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        second_l = [] # this list will contain all the unique number of bits of the arr
        dic = {} # making a dictionary of {number of bits: [list of elements with those bits]}
        
        # populating the dic dictionary
        for i in arr:
            bits = bin(i).count("1")
            if dic.__contains__(bits):
                dic[bits].append(i)
            else:
                dic[bits] = [i]
    
        # iterating over the dictioary
        for i in dic:
            second_l.append(i) # adding elements to second list
            dic[i].sort() # sorting the value list in the dictionary

        second_l.sort()
        ans = []
        for i in second_l:
            for elem in dic[i]:
                ans.append(elem) # finally adding the elements from sort list of dictionary values 
                
        return ans