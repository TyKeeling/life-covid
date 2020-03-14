import numpy as np
import random

class classroom():

    def __init__(self, x, y, rate, num_infected=0):
        self.rate = rate # each person (of 8) infected with probability "rate"
        self.arr = np.zeros((y,x), dtype=bool)

        while (np.sum(self.arr) < num_infected):
            self.arr[random.randint(0,y-1),random.randint(0,x-1)] = True

        self.infected_per_round = num_infected
        self.total_infected = num_infected
        self.total_population = x*y

    def iterate(self):

        newarr = np.zeros_like(self.arr)

        for x in range(0, self.arr.shape[1]):
            for y in range(0, self.arr.shape[0]):
                if self.arr[y,x] == True:
                    newarr[y,x] = True
                    # Corner Transmission: 
                    if x > 0 and y > 0:
                        newarr[y-1,x-1] = self.chance() or self.arr[y-1,x-1]
                    if x > 0 and y < (self.arr.shape[1] - 1):
                        newarr[y+1,x-1] = self.chance() or self.arr[y+1,x-1]
                    if x < (self.arr.shape[0] - 1) and y > 0:
                        newarr[y-1,x+1] = self.chance() or self.arr[y-1,x+1]
                    if x < (self.arr.shape[0] - 1) and y < (self.arr.shape[1] - 1):
                        newarr[y+1,x+1] = self.chance() or self.arr[y+1,x+1]

                    # Horizontal Transmission
                    if x > 0:
                        newarr[y,x-1] = self.chance() or self.arr[y,x-1]
                    if x < (self.arr.shape[0] - 1):
                        newarr[y,x+1] = self.chance() or self.arr[y,x-1]

                    # Vertical Transmission
                    if y > 0:
                        newarr[y-1,x] = self.chance() or self.arr[y-1,x]
                    if y < (self.arr.shape[0] - 1):
                        newarr[y+1,x] = self.chance() or self.arr[y+1,x]

        self.infected_per_round = np.sum(self.arr) - np.sum(newarr)
        self.total_infected = np.sum(newarr)
        self.arr = newarr

    def chance(self):
        if random.random() <= self.rate:
            return True
        return False

if __name__ == "__main__":
    # Some tests
    g = classroom(8, 8, 0.5, 1)
    print(g.arr)
    print("\n")
    for i in range(0,2):
        g.iterate()
        print(g.arr)
        print("\n")


    # arr = np.zeros((2,2), dtype=bool)
    # arr[0,1] = True
    # print(arr)
    pass