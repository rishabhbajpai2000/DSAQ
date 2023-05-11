from queue import LifoQueue
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = LifoQueue()
        stack2 = LifoQueue()

        for i in s:
            if i =="#": 
                if stack1.empty() == False: stack1.get()
                else: pass
            else: stack1.put(i)

        for i in t:
            if i =="#": 
                if stack2.empty() == False: stack2.get()
                else: pass
            else: stack2.put(i)

        if stack1.qsize() != stack2.qsize():return False

        while stack1.empty() != True:
            if stack1.get() != stack2.get():return False
        return True