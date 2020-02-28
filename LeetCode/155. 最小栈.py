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
        self.stack = [0]*100
        self.pointTop = -1
        self.pointMin = -1
        self.nowSize = 0
        self.SIZE = 100

    def push(self, x: int) -> None:
        if(self.nowSize >= self.SIZE):
            return False
        else:
            self.nowSize += 1
        self.pointTop += 1
        if(self.pointMin == -1):
            self.pointMin = 0
        else:
            if(self.stack[self.pointMin] > x):
                self.pointMin = self.pointTop
        self.stack[self.pointTop] = x
        return True

    def pop(self) -> None:
        if(self.nowSize <= 0):
            return None
        else:
            if(self.pointTop == self.pointMin):
                min = self.stack[0]
                self.pointMin = 0
                for i in range(self.nowSize - 1):
                    if(min > self.stack[i]):
                        min = self.stack[i]
                        self.pointMin = i
            self.nowSize -= 1
            self.pointTop -= 1
            if(self.nowSize == 0):
                self.pointMin = -1
        return self.stack[self.nowSize]

    def top(self) -> int:
        if(self.nowSize <= 0):
            return None
        else:
            return self.stack[self.pointTop]

    def getMin(self) -> int:
        if(self.pointTop == -1):
            return None
        else:
            return self.stack[self.pointMin]

    def printStack(self):
        print(self.stack)


def main():
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


main()
