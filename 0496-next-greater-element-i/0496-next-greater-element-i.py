class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        
        for tocheck in nums1:
            position = 0
            for index in range(len(nums2)):
                if nums2[index] == tocheck:
                    position = index
                    break
            
            found = False
            for element in range(position +1, len(nums2)):
                if nums2[element]>tocheck:
                    answer.append(nums2[element])
                    found = True
                    break
            if found == False: answer.append(-1)
                
        return answer