import numpy as np

BOARD = np.zeros([15, 15])
class person:
    color = None                #the color of chess piece
    is_on = True            
    points = 0                  #the points you got
    poss=np.zeros([15, 15])                   #the possibility of every poisition in the board
    child1 = np.random.uniform(0, 0.1, [14])
    child2 = np.random.uniform(0, 0.1, [14])

    def __init__(self, c1, c2, color = 1):       #init the infomation
        global BOARD
        BOARD = np.zeros([15, 15])
        self.color = color
        self.points = 0

        self.child1 = c1
        self.child2 = c2

        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        self.poss[x, y] = 0.01

    def put_down(self, x, y, object):            #after putting down your chess piece
        BOARD[x, y] = self.color

        self.poss_updata(x, y, object)

        is_win = self.check(x, y)

        if(is_win):                             #plus the point
            # print(self.color,"win")
            self.points += 1
            self.clear(object)
        else:
            # print("\nNo win:",self.color)
            pass
        
        
        # print("poss1:",self.poss)
        # print("poss2:",object.poss)

        

        return is_win

    def poss_updata(self, x, y, object):              #upgrade the possibility of person1 and person
        for i in range(15):
            for j in range(15):
                if i == x and j == y:
                    self.poss[x, y] = -1
                elif abs(i - x) < abs(j - y):
                    if self.poss[i, j] == -1:
                        pass
                    else:
                        self.poss[i, j] = self.child1[j - 1]
                else:
                    if self.poss[i, j] == -1:
                        pass
                    else:
                        self.poss[i, j] = self.child1[i - 1]

        for i in range(15):
            for j in range(15):
                if i == x and j == y:
                    object.poss[x, y] = -1
                elif abs(i - x) < abs(j - y):
                    if object.poss[i, j] == -1:
                        pass
                    else:
                        object.poss[i, j] = object.child2[j - 1]
                else:
                    if object.poss[i, j] == -1:
                        pass
                    else:
                        object.poss[i, j] = object.child2[i - 1]

        return None



        pass
    
    def check(self, x, y):
        direction = [[1,1],[1,-1],[1,0]]
        is_win = False
        for direct in direction:
            chess = 1
            x_temp = x
            y_temp = y
            while (0 <= x_temp + direct[0] <= 14) and (0 <= y_temp + direct[1] <= 14) and (BOARD[x_temp + direct[0], y_temp + direct[1]] == self.color):
                chess += 1
                x_temp += direct[0]
                y_temp += direct[1]
            
            x_temp = x
            y_temp = y
            while (0 <= x_temp - direct[0] <= 14) and (0 <= y_temp - direct[1] <= 14) and (BOARD[x_temp - direct[0], y_temp - direct[1]] == self.color):
                chess += 1
                x_temp -= direct[0]
                y_temp -= direct[1]

            
            if chess >= 5:
                is_win = True
                break
        
        return is_win

    def print_point(self):
        print(self.poss)

    def print_color(self):
        print(self.color)

    def print_child(self):
        print(self.child)


    def clear(self, object):
        global BOARD 
        BOARD = np.zeros([15, 15])
        self.poss = np.zeros([15, 15])
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        self.poss[x, y] = 0.01

        object.poss = np.zeros([15, 15])
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        object.poss[x, y] = 0.01

    def get_poisition(self):
        x, y = np.unravel_index(np.argmax(self.poss, axis=None), self.poss.shape)
        return (x, y)

    
    def main(self, object):
        x, y = self.get_poisition()
        # print(x,y)
        is_win = self.put_down(x, y, object)

        return is_win



class AI:
    parents = np.random.uniform(0, 0.1, [10, 2, 14])
    p_fitness = np.zeros([14])

    def __init__(self, x):
        self.parents = np.random.uniform(0, 0.1, [10, 2, 14])
        self.p_fitness = np.zeros([14])

    def crossover(self):                        #chose two parentsDNA
        pass


    def mutate(self):
        print(np.random.choice(a=5, size=5, replace=False, p=None))
        pass

    def get_fitness_first(self, child1, child2):
        p1 = person(child1[0], child1[1], 1)
        p2 = person(child2[0], child2[1], -1)
        # print(BOARD)
        is_win = False
        for i in range(50):
            for j in range(50):
                if(p1.main(p2)):
                    break
                if(p2.main(p1)):
                    break
                if j == 99:
                    p1.clear(p2)
            
            for j in range(100):
                if(p2.main(p1)):
                    break
                if(p1.main(p2)):
                    break
                if i == 99:
                    p1.clear(p2)
        return (p1.points, p2.points)

    def get_fitness(self):
        for i in range(10):
            for j in range(10):
                x, y = self.get_fitness_first(self.parents[i], self.parents[j])
                if (x + y) != 0:
                    self.p_fitness[i] += (x / (x + y))
                    self.p_fitness[j] += (y / (x + y))
                    print(i,":",j,"=",x, y)
        print(self.p_fitness)


def main():
    
    a = AI(1)
    a.get_fitness()
    # p1 = person(1)
    # p2 = person(-1)
    # is_win = False
    # for i in range(100):
    #     for j in range(50):
    #         if(p1.main(p2)):
    #             break
    #         if(p2.main(p1)):
    #             break

    #     for j in range(50):
    #         if(p2.main(p1)):
    #             break
    #         if(p1.main(p2)):
    #             break
    #         # p1.print_point()
    #         # print("\n")
    #         # p2.print_point()
    
    # print(BOARD)
    # p1.print_child()
    # p2.print_child()


main()

