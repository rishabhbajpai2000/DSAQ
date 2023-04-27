class MyQueue:

    def __init__(self):
        self.mainStack = []
        self.secondStack = []

    def push(self, x: int) -> None:
        self.mainStack.append(x)
        

    def pop(self) -> int:
        while self.mainStack:
            self.secondStack.append(self.mainStack[-1])
            self.mainStack.pop()
            
        toreturn = self.secondStack[-1]
        self.secondStack.pop()
        while self.secondStack:
            self.mainStack.append(self.secondStack[-1])
            self.secondStack.pop()
            
        print(self.secondStack)
        return toreturn
        

    def peek(self) -> int:
        return self.mainStack[0]

    def empty(self) -> bool:
        return len(self.mainStack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()