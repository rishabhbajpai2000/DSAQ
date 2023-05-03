from queue import Queue
class MyStack:

    def __init__(self):
        self.que_main = Queue()
        self.que_sec = Queue()

    def push(self, x: int) -> None:
        while self.que_main.empty() != True:
            self.que_sec.put(self.que_main.get())
        
        self.que_main.put(x)
        
        while (self.que_sec.empty() != True): 
            self.que_main.put(self.que_sec.get())
        

    def pop(self) -> int:
        return self.que_main.get()
    
    def top(self) -> int:
        return self.que_main.queue[0]

    def empty(self) -> bool:
        return self.que_main.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()