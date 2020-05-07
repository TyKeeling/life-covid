import numpy as np
import random

import Classroom

class University():

    def __init__(self, square_length, num_classrooms,  
        rate, drifters=(square_length*square_length/10), num_infected=1):

        self.class_list = []
        self.rate = rate

        for i in range(num_classrooms):
            if i < num_infected:
                class_list.append(Classroom.classroom(square_length, square_length, rate, 1))
            else:
                class_list.append(Classroom.classroom(square_length, square_length, rate, 0))

    def iterate(self):
        for room in class_list:
            room.iterate()

    def drift(self):
        coords = np.zeros((people_per_classroom, len(classrooms),  2), dtype=np.uint8)
        # boolist = np.zeros((people_per_classroom, len(classrooms)), dtype=np.bool)

        #need two unique points 
        for j in range(len(classrooms)):
            for i in range(people_per_classroom):
                do = True
                while do:
                    coords[i,j,0] = random.randint(0, classrooms[j].x)
                    coords[i,j,1] = random.randint(0, classrooms[j].y)
                    print(coords[i,j], "in ", coords[0:i,j], "? ", coords[i,j] in coords [0:i,j])
                    
                    do = False and coords[i,j] in coords [0:i-1,j]

            print(coords[:,j,0], coords[:,j,1], "\n")

