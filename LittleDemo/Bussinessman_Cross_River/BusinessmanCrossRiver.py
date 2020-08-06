AVAILABLE = 1
NOT_AVAILABLE = 0


class BussinessmanCrossRiver():
    def __init__(self, busmanSum: int, servantSum: int, boatSum: int):
        self.busmanSum = busmanSum
        self.servantSum = servantSum
        self.boatSum = boatSum
        self.initGraph()
        # record every step
        self.process = []
        self.DSP(busmanSum, servantSum, 0, 0, True)
        for p in self.process:
            print(p)

    def initGraph(self):
        self.thisGraph = []
        # 初始化此岸数据
        for i in range(self.busmanSum + 1):
            self.thisGraph.append([[]] * (self.servantSum + 1))
            for j in range(self.servantSum + 1):
                if(i == 0 or i >= j):
                    self.thisGraph[i][j] = []
                else:
                    self.thisGraph[i][j] = NOT_AVAILABLE
        # 初始化彼岸数据
        self.thatGraph = []
        for i in range(self.busmanSum + 1):
            self.thatGraph.append([[]] * (self.servantSum + 1))
            for j in range(self.servantSum + 1):
                if(i == 0 or i >= j):
                    self.thatGraph[i][j] = []
                else:
                    self.thatGraph[i][j] = NOT_AVAILABLE

    def DSP(self, thisX: int, thisY: int, thatX: int, thatY: int,
            direction: bool):
        # 终止递归的条件
        if(thisX == 0 and thisY == 0):
            return True

        # 船上的商人数量
        for XBoatNum in range(self.boatSum + 1):
            # 船上的仆人数量
            for YBoatNum in range(self.boatSum - XBoatNum + 1):
                # 防止出现(0, 0)情况
                if(XBoatNum + YBoatNum == 0):
                    continue
                if(direction is True):
                    # 此岸商人数量
                    XThisNum = thisX - XBoatNum
                    if(XThisNum < 0):
                        continue
                    # 此岸仆人数量
                    YThisNum = thisY - YBoatNum
                    if(YThisNum < 0):
                        continue
                    # 彼岸商人数量
                    XThatNum = thatX + XBoatNum
                    if(XThatNum < 0):
                        continue
                    # 彼岸仆人数量
                    YThatNum = thatY + YBoatNum
                    if(YThatNum < 0):
                        continue
                else:
                    # 此岸商人数量
                    XThisNum = thisX + XBoatNum
                    if(XThisNum < 0):
                        continue
                    # 此岸仆人数量
                    YThisNum = thisY + YBoatNum
                    if(YThisNum < 0):
                        continue
                    # 彼岸商人数量
                    XThatNum = thatX - XBoatNum
                    if(XThatNum < 0):
                        continue
                    # 彼岸仆人数量
                    YThatNum = thatY - YBoatNum
                    if(YThatNum < 0):
                        continue
                # 可行
                if(self.thisGraph[XThisNum][YThisNum]
                   != NOT_AVAILABLE and
                   self.thatGraph[XThatNum][YThatNum]
                   != NOT_AVAILABLE and
                   # 判断是否重复
                   self.isRepeat(self.thisGraph[thisX][thisY],
                                 (thatX, thatY, direction, XBoatNum, YBoatNum))
                   is False):
                    # 打印语句
                    if(direction is True):
                        self.process.append('(%d,%d)-->[%d,%d]-->(%d,%d)' %
                                            (thisX, thisY, XBoatNum,
                                             YBoatNum, thatX, thatY))
                    else:
                        self.process.append('(%d,%d)<--[%d,%d]<--(%d,%d)' %
                                            (thisX, thisY, XBoatNum,
                                             YBoatNum, thatX, thatY))
                    self.thisGraph[thisX][thisY].append((thatX, thatY,
                                                         direction,
                                                         XBoatNum,
                                                         YBoatNum))
                    isOK = self.DSP(XThisNum, YThisNum, XThatNum,
                                    YThatNum, not direction)
                    # 路径有效
                    if(isOK is True):
                        return True
                    # 路径无效
                    else:
                        self.delete(self.thisGraph[thisX][thisY],
                                    (thatX, thatY, direction, XBoatNum,
                                     YBoatNum))
                        self.process.pop()
                        continue

    def isRepeat(self, listt: list, path) -> bool:
        for p in listt:
            if(p == path):
                return True
        return False

    def delete(self, listt: list, path):
        listt.remove(path)


if __name__ == "__main__":
    b = BussinessmanCrossRiver(6, 5, 2)
