def givecontainer(pattern):
    index = 0
    container = [[pattern[0],1]]
    while index < len(pattern)-1:
        next_index = index + 1 
        if pattern[next_index] == pattern[index]:
            container[-1][1] += 1
        else:
            container.append([pattern[index+1],1])
        index += 1
    
    return container
        
        
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name): return False
        
        container1 = givecontainer(name)
        container2 = givecontainer(typed)
        
        
        if len(container1) != len(container2): return False
        
        for i in range(len(container1)):
            if container1[i][0] != container2[i][0]: return False
            if container1[i][1] > container2[i][1]: return False
            
        return True
        