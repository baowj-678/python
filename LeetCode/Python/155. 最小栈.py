# 155. 最小栈
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.


class MinStack:
    def __init__(self):
        self.pointNow = 0
        self.stack = []
        self.minElement = []
        self.nowSize = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        if(self.nowSize > 0):
            if(x < self.minElement[-1]):
                self.minElement.append(x)
            else:
                self.minElement.append(self.minElement[-1])
        else:
            self.minElement.append(x)
        self.nowSize += 1

    def pop(self) -> None:
        if(self.nowSize <= 0):
            return None
        else:
            self.stack.pop(-1)
            self.minElement.pop(-1)
            self.nowSize -= 1

    def top(self) -> int:
        if(self.nowSize <= 0):
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if(self.nowSize <= 0):
            return None
        else:
            return self.minElement[-1]

    def printStack(self):
        print(self.stack)


if __name__ == '__main__':
    stack = MinStack()
    while(True):
        i = eval(input("1.push;\n2.pop;\n3.top;\n4.getMin;\n5.printStack;\n\
6.exit;\n"))
        if(i == 6):
            break
        else:
            if(i == 1):
                x = eval(input("input:"))
                print(stack.push(x))
            elif(i == 2):
                print(stack.pop())
            elif(i == 3):
                print(stack.top())
            elif(i == 4):
                print(stack.getMin())
            else:
                stack.printStack()
