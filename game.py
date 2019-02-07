from class_item.target import target
from class_item.target_item.bezier import bezier

import numpy as np
import math as mt
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import csv
#'''
import matplotlib.animation as animation
from matplotlib import animation
#'''
class game(object):
    """docstring for game_class."""
    dt = 0
    def __init__(self, dt):
        self.dt = dt
    def run(self, anime):
        print("+++ game start")
        ##init #################################################################
        bz = bezier(number_of_points=5000)
        tg = target(self.dt)
        ##init bezier###########################################################
        BEZIER_ANCER1 = np.array([[0,0],[0,1.4],[-1.43,0.1],[-1.43,1.5]], dtype=np.float)
        BEZIER_ANCER2 = np.array([[-1.43,1.5],[-1.43,2.9],[-0.01,1.6],[-0.01,3.0]], dtype=np.float)
        BEZIER_ANCER3 = np.array([[-0.01,3.0],[-0.01,4.4],[-1.43,3.1],[-1.43,4.5]], dtype=np.float)
        BEZIER_ANCER4 = np.array([[-1.43,4.5],[-1.43,5.9],[-0.725,4.6],[-0.725,6.0]], dtype=np.float)

        BEZIER1 = bz.bezier_making(BEZIER_ANCER1, 3)
        BEZIER2 = bz.bezier_making(BEZIER_ANCER2, 3)
        BEZIER3 = bz.bezier_making(BEZIER_ANCER3, 3)
        BEZIER4 = bz.bezier_making(BEZIER_ANCER4, 3)
        ##init accel_designer###################################################
        xs = 0.0                                #x start
        ts = 0.0                                #t start
        '''1
        A  = [1.0, 1.0, 1.0, 1.0]
        VEL=[[1.0, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [1.0, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.0, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.0, 0.6, 0.6]]                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
        #'''

        #'''2
        A  = [2.0, 2.0, 2.0, 2.0]
        VEL=[[2.2, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [2.2, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [2.2, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [2.0, 0.6, 0.6]]                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
        #'''
        BEZIER=[BEZIER1, BEZIER2, BEZIER3, BEZIER4]
        ##def target_make(self, a, BEZIER, VEL, x_start, time_start, num):   * a := float
        REF, t, x, vx, vy, alfa = tg.target_make(A, VEL, BEZIER, xs, ts, 4)
        npREF = np.array(REF)

        print("game time  := {}[s]".format(t))
        print("game lenge := {}[m]".format(x))
        self.plot(npREF)

        with open('csv_item/x_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npREF.T[0])
        with open('csv_item/y_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npREF.T[1])
        '''
        with open('csv_item/test.csv', 'w') as f:
            writer = csv.writer(f)
            #writer.writeheader()
            writer.writerow(NEW_LOBS.T[0])
            writer.writerow(NEW_LOBS.T[1])
        '''
        ##csv###################################################################
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(alfa)
        ########################################################################
        if anime == True:
            #self.plot_size(npREF)
            self.anime_ff(vx, vy, alfa)
        print("+++ end game")
    def run_line(self, anime):
        print("+++ game start")
        ##init #################################################################
        num = 5000
        bz = bezier(number_of_points=num)
        tg = target(self.dt)
        ##init bezier###########################################################
        BEZIER_ANCER1= np.array([[0,0],[0,1.43 -0.7],[-1.43,0.1 -0.4],[-1.43,1.0]], dtype=np.float)
        LINE_ANCER1  = [-1.43, 1.0, 2.0, num]
        BEZIER_ANCER2= np.array([[-1.43,2.0],[-1.43,2.0 +0.5],[-0.01,2.5 -0.5],[-0.01,2.5]], dtype=np.float)
        LINE_ANCER2  = [-0.01, 2.5, 3.5, num]
        BEZIER_ANCER3= np.array([[-0.01,3.5],[-0.01,3.5 +0.5],[-1.43,4.0 -0.5],[-1.43,4.0]], dtype=np.float)
        LINE_ANCER3  = [-1.43, 4.0, 5.0, num]
        BEZIER_ANCER4= np.array([[-1.43,5.0],[-1.43,5.9 -0.6],[-0.725,6.0 -0.6],[-0.725,6.0]], dtype=np.float)


        BEZIER1= bz.bezier_making(BEZIER_ANCER1, 3)
        LINE1  = self.line_making(LINE_ANCER1)
        BEZIER2= bz.bezier_making(BEZIER_ANCER2, 3)
        LINE2  = self.line_making(LINE_ANCER2)
        BEZIER3= bz.bezier_making(BEZIER_ANCER3, 3)
        LINE3  = self.line_making(LINE_ANCER3)
        BEZIER4= bz.bezier_making(BEZIER_ANCER4, 3)
        ##init accel_designer###################################################
        xs = 0.0                                #x start
        ts = 0.0                                #t start
        '''1
        A =[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        VEL=[[1.4, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [1.1, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.4, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.1, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.4, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.1, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.2, 0.6, 0.6]]                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
        #'''

        '''2
        A =[1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 1.0]
        VEL=[[1.4, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [1.5, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.4, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.5, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.4, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.5, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.2, 0.6, 0.6]]                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
        #'''

        #'''3
        A =[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
        VEL=[[1.6, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [1.5, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.5, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.5, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.5, 0.6, 0.6]]                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
        #'''
        BEZIER=[BEZIER1, LINE1, BEZIER2, LINE2, BEZIER3, LINE3, BEZIER4]
        ##def target_make(self, a, BEZIER, VEL, x_start, time_start):   * a := float
        REF, t, x, vx, vy, alfa = tg.target_make(A, VEL, BEZIER, xs, ts, 7)
        npREF = np.array(REF)

        print("game time  := {}[s]".format(t))
        print("game lenge := {}[m]".format(x))
        self.plot(npREF)

        with open('csv_item/x_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npREF.T[0])
        with open('csv_item/y_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npREF.T[1])
        '''
        with open('csv_item/test.csv', 'w') as f:
            writer = csv.writer(f)
            #writer.writeheader()
            writer.writerow(NEW_LOBS.T[0])
            writer.writerow(NEW_LOBS.T[1])
        '''
        ##csv###################################################################
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(alfa)
        ########################################################################

        if anime == True:
            self.plot_size(npREF)
            self.anime_ff(vx, vy, alfa)
        print("+++ end game")
    def run_cal(self, anime):
        print("+++ game start")
        ##init #################################################################
        num = 10000
        bz = bezier(number_of_points=num)
        tg = target(self.dt)
        ##init bezier###########################################################
        xc = -0.725
        yc=[1.5, 3.0, 4.5]
        r=0.53 +0.1
        CIRCLE0 = self.circle_making(xc, yc, r, 0)
        CIRCLE1 = self.circle_making(xc, yc, r, 1)
        CIRCLE2 = self.circle_making(xc, yc, r, 2)
        #print(CIRCLE0[0], CIRCLE0[len(CIRCLE0)-1])
        #print(CIRCLE0[0][0], CIRCLE0[0][1])

        xl0 = [0.0, CIRCLE0[0][0]]
        yl0 = [0.0, CIRCLE0[0][1]]
        xl1 = [CIRCLE0[len(CIRCLE0)-1][0], CIRCLE1[0][0]]
        yl1 = [CIRCLE0[len(CIRCLE0)-1][1], CIRCLE1[0][1]]
        xl2 = [CIRCLE1[len(CIRCLE1)-1][0], CIRCLE2[0][0]]
        yl2 = [CIRCLE1[len(CIRCLE1)-1][1], CIRCLE2[0][1]]

        LINE0  = self.line_making2(xl0, yl0, num)
        LINE1  = self.line_making2(xl1, yl1, num)
        LINE2  = self.line_making2(xl2, yl2, num)
        #BEZIER_ANCER1 = np.array([[0,0],[0,1.4],[-1.43,0.1],[-1.43,1.5]], dtype=np.float)
        #BEZIER4 = bz.bezier_making(BEZIER_ANCER4, 3)
        ##init accel_designer###################################################
        xs = 0.0                                #x start
        ts = 0.0                                #t start

        '''1
        A  = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        VEL=[[1.3, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.1, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.1, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6]]
        #'''
        '''1:1.0
        A  = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        VEL=[[1.4, 0.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.3, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.3, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0]]
        #'''
        '''2
        A  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0]

        VEL=[[1.7, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.4, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.4, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6]]
        #'''
        '''2:1.0
        A  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0]

        VEL=[[1.8, 0.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.6, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.6, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0]]
        #'''
        '''3
        A  = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0]

        VEL=[[2.0, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.5, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.5, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6]]
        #'''
        #'''3:1.0
        A  = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0]

        VEL=[[2.2, 0.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.8, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.8, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0]]
        #'''

        BEZIER = [LINE0, CIRCLE0, LINE1, CIRCLE1, LINE2, CIRCLE2]
        ##def target_make(self, a, BEZIER, VEL, x_start, time_start, num):   * a := float
        REF, t, x, vx, vy, alfa = tg.target_make(A, VEL, BEZIER, xs, ts, 6)
        npREF = np.array(REF)

        print("game time  := {}[s]".format(t))
        print("game lenge := {}[m]".format(x))
        self.plot(npREF)

        with open('csv_item/x_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npREF.T[0])
        with open('csv_item/y_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npREF.T[1])
        '''
        with open('csv_item/test.csv', 'w') as f:
            writer = csv.writer(f)
            #writer.writeheader()
            writer.writerow(NEW_LOBS.T[0])
            writer.writerow(NEW_LOBS.T[1])
        '''
        ##csv###################################################################
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(alfa)
        ########################################################################
        if anime == True:
            self.plot_size(npREF)
            self.anime_ff(vx, vy, alfa)
        print("+++ end game")
    def run_calab(self, anime):
        print("+++ game start")
        ##init #################################################################
        num = 1000
        bz = bezier(number_of_points=num)
        tg = target(self.dt)
        ##init circle###########################################################
        xc = -0.725
        yc=[1.5, 3.0, 4.5]
        r=0.53 +0.1
        CIRCLE0 = self.circle_making2(xc, yc, r, 0)
        CIRCLE1 = self.circle_making2(xc, yc, r, 1)
        CIRCLE2 = self.circle_making2(xc, yc, r, 2)
        ##init line#############################################################
        xl0 = [0.0, CIRCLE0[0][0]]
        yl0 = [0.0, CIRCLE0[0][1]]
        LINE0  = self.line_making2(xl0, yl0, num)
        ##init bezier###########################################################
        BEZIER_ANCER0 = np.array([[CIRCLE0[len(CIRCLE0)-1][0], CIRCLE0[len(CIRCLE0)-1][1]],
                             [CIRCLE0[len(CIRCLE0)-1][0], CIRCLE0[len(CIRCLE0)-1][1] +0.5],
                             [CIRCLE0[len(CIRCLE0)-1][0] -xc, CIRCLE0[len(CIRCLE0)-1][1] +0.75],
                             [CIRCLE1[0][0],CIRCLE1[0][1]]], dtype=np.float)
        BEZIER_ANCER1 = np.array([[CIRCLE1[len(CIRCLE1)-1][0], CIRCLE1[len(CIRCLE1)-1][1]],
                                 [CIRCLE1[len(CIRCLE1)-1][0], CIRCLE1[len(CIRCLE1)-1][1] +0.5],
                                 [CIRCLE1[len(CIRCLE1)-1][0] +xc, CIRCLE1[len(CIRCLE1)-1][1] +0.75],
                                 [CIRCLE2[0][0],CIRCLE2[0][1]]], dtype=np.float)

        BEZIER_ANCER2 = np.array([[CIRCLE2[len(CIRCLE2)-1][0], CIRCLE2[len(CIRCLE2)-1][1]],
                                 [CIRCLE2[len(CIRCLE2)-1][0], CIRCLE2[len(CIRCLE2)-1][1] +0.75],
                                 [xc, CIRCLE2[len(CIRCLE2)-1][1] +0.75 -0.2],
                                 [xc,6.0]], dtype=np.float)
        BEZIER0 = bz.bezier_making(BEZIER_ANCER0, 3)
        BEZIER1 = bz.bezier_making(BEZIER_ANCER1, 3)
        BEZIER2 = bz.bezier_making(BEZIER_ANCER2, 3)
        #BEZIER_ANCER1 = np.array([[0,0],[0,1.4],[-1.43,0.1],[-1.43,1.5]], dtype=np.float)
        #BEZIER4 = bz.bezier_making(BEZIER_ANCER4, 3)
        ##init accel_designer###################################################
        xs = 0.0                                #x start
        ts = 0.0                                #t start

        #'''1
        A  = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        VEL=[[1.3, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.3, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.3, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],
             [0.6, 0.6, 0.6]]
        #'''
        '''1:1.0
        A  = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        VEL=[[1.4, 0.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.5, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.5, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],
             [1.0, 1.0, 1.0]]
        #'''
        '''2
        A  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]

        VEL=[[1.7, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [1.7, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.7, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],
             [0.6, 0.6, 0.6]]
        #'''
        '''2:1.0
        A  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]

        VEL=[[1.8, 0.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.9, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [1.9, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],
             [1.0, 1.0, 1.0]]
        #'''
        '''3
        A  = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]

        VEL=[[2.0, 0.0, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [2.0, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],                   #vell_want, vell_start, vell_end 0.7, 0.6, 0.6
             [2.0, 0.6, 0.6],                   #vell_want, vell_start, vell_end
             [0.6, 0.6, 0.6],
             [0.6, 0.6, 0.6]]
        #'''
        '''3:1.0
        A  = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]

        VEL=[[2.2, 0.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [2.2, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [2.2, 1.0, 1.0],                   #vell_want, vell_start, vell_end
             [1.0, 1.0, 1.0],
             [1.0, 1.0, 1.0]]
        #'''

        BEZIER = [LINE0, CIRCLE0, BEZIER0, CIRCLE1, BEZIER1, CIRCLE2, BEZIER2]
        ##def target_make(self, a, BEZIER, VEL, x_start, time_start, num):   * a := float
        REF, t, x, vx, vy, alfa = tg.target_make(A, VEL, BEZIER, xs, ts, 7)
        npREF = np.array(REF)

        print("game time  := {}[s]".format(t))
        print("game lenge := {}[m]".format(x))
        self.plot(npREF)

        with open('csv_item/x_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npREF.T[0])
        with open('csv_item/y_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npREF.T[1])
        '''
        with open('csv_item/test.csv', 'w') as f:
            writer = csv.writer(f)
            #writer.writeheader()
            writer.writerow(NEW_LOBS.T[0])
            writer.writerow(NEW_LOBS.T[1])
        '''
        ##csv###################################################################
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(alfa)
        ########################################################################
        if anime == True:
            self.plot_size(npREF)
            self.anime_ff(vx, vy, alfa)
        print("+++ end game")
    def circle_making(self, xc, yc , r, i):
        d1=np.sqrt(xc**2 +yc[0]**2)
        d=1.5
        t=mt.acos(r/d1)
        te=mt.asin(abs(xc)/d1)
        t1=t-te
        t2=mt.acos(2*r/d)
        CIRCLE = []
        if i == 0:
            for theta in np.arange(0.0, 2*np.pi, 2*np.pi/5000.0):
                if theta >= t1 and theta <= np.pi -t2:
                    x = r* -np.sin(theta) +xc
                    y = r* -np.cos(theta) +yc[i]
                    CIRCLE.append([x,y])
        elif i==1:
            for theta in np.arange(0.0, 2*np.pi, 0.01):
                if theta >= t2 and theta <= np.pi -t2:
                    x = r* np.sin(theta) +xc
                    y = r* -np.cos(theta) +yc[i]
                    CIRCLE.append([x,y])
        elif i==2:
            for theta in np.arange(0.0, 2*np.pi, 0.01):
                if theta >= t2 and theta <= np.pi -t2:
                    x = r* -np.sin(theta) +xc
                    y = r* -np.cos(theta) +yc[i]
                    CIRCLE.append([x,y])
        else:
            print("circle_making arror\n")
        return CIRCLE
    def circle_making2(self, xc, yc , r, i):
        d1=np.sqrt(xc**2 +yc[0]**2)
        d=1.5
        t=mt.acos(r/d1)
        te=mt.asin(abs(xc)/d1)
        t1=t-te
        t2=mt.acos(2*r/d)
        CIRCLE = []
        if i ==0:
            for theta in np.arange(0.0, 2*np.pi, 2*np.pi/5000.0):
                if theta >= t1 and theta <= np.pi/2:
                    x = r* -np.sin(theta) +xc
                    y = r* -np.cos(theta) +yc[i]
                    CIRCLE.append([x,y])
        elif i==1:
            for theta in np.arange(0.0, 2*np.pi, 0.01):
                if theta >= t2 and theta <= np.pi/2:
                    x = r* np.sin(theta) +xc
                    y = r* -np.cos(theta) +yc[i]
                    CIRCLE.append([x,y])
        elif i==2:
            for theta in np.arange(0.0, 2*np.pi, 0.01):
                if theta >= t2 and theta <= np.pi/2:
                    x = r* -np.sin(theta) +xc
                    y = r* -np.cos(theta) +yc[i]
                    CIRCLE.append([x,y])
        else:
            print("circle_making arror\n")
        return CIRCLE
    def line_making2(self, xl, yl, num):
        LINE2=[]
        x = np.linspace(xl[0], xl[1], num)
        y = np.linspace(yl[0], yl[1], num)
        for index in np.arange(0, len(x), 1):
            LINE2.append([x[index], y[index]])
        return LINE2
    def line_making(self, LINE_ANCER):
        LINE = []
        x = LINE_ANCER[0]
        for y in np.linspace(LINE_ANCER[1], LINE_ANCER[2], LINE_ANCER[3]):
            LINE.append([x, y])
        return LINE
    def plot(self, npREF):
        plt.show()
        #plt.hold(True)
        plt.plot(npREF.T[0],npREF.T[1], marker=".", color="#4278C5")
        plt.title("ref")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
    def plot_size(self, npREF):
        ########################################################################
        ########################################################################
        ###########################     model     ##############################
        ########################################################################
        #'''
        ax = plt.axes()
        COUNT = np.arange(start=0, stop=len(npREF) -1, step=1, dtype= int)
        ssp=[-0.5,-0.5]
        for count in COUNT:
            r = patches.Rectangle(xy=(npREF.T[0][count] -0.35,npREF.T[1][count] -0.35), width=0.7, height=0.7, ec='#F5A9A9', fill=False)
            ax.add_patch(r)
            #c = patches.Circle(xy=(npNEW_LOB.T[0][count],npNEW_LOB.T[1][count]), radius=0.4, ec='#F5A9A9',fill=False)
            #ax.add_patch(c)
        ############################     field     #############################
        ########################################################################
        sotowaku = patches.Rectangle(xy=(-13.3+0.5,-0.5), width=13.3, height=10, ec='#FAAC58',fill=False)
        ax.add_patch(sotowaku)
        forest = patches.Rectangle(xy=(-2.45+0.5,-0.5), width=2.45, height=8, ec='#FAAC58',fill=False)
        ax.add_patch(forest)
        bridge = patches.Rectangle(xy=(-1.725 +0.5, 6.5 -0.5), width=1, height=1.5, ec='#FAAC58',fill=False)
        ax.add_patch(bridge)
        bri1 = patches.Circle(xy=(-1.725 +0.5, 6.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri1)
        bri2 = patches.Circle(xy=(-1.725 +0.5, 6.5+1.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri2)


        d = patches.Circle(xy=(-1*(1.225+ssp[0]),2+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(d)
        e = patches.Circle(xy=(-1*(1.225+ssp[0]),3.5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(e)
        f = patches.Circle(xy=(-1*(1.225+ssp[0]),5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(f)
        #'''
        ########################################################################
        ########################################################################
        ########################################################################
        plt.axis("equal")
        plt.grid(True)
        plt.show()
    def anime_ff(self, vx, vy, alfa):
        #'''#FF
        fig = plt.figure()
        ims = []
        X = []
        Y = []
        x=0
        y=0
        ssp=[-0.5,-0.5]
        #V = self.target.get_V()
        for index in np.arange(start=1, stop=len(vx)-1, step=1, dtype= int):
            x = x + vx[index] * self.dt
            y = y + vy[index] * self.dt
            X.append(x)
            Y.append(y)

            #vehi = np.matrix([[0.4, 0.4, -0.4, -0.4],[0.4, -0.4, -0.4, 0.4]])
            vehi = np.matrix([[0, 0.35, 0.35, -0.35, -0.35, 0],[0.7, 0.35, -0.35, -0.35, 0.35, 0.7]])
            Rot = np.matrix([[np.cos(-alfa[index]),-np.sin(-alfa[index])],[np.sin(-alfa[index]),np.cos(-alfa[index])]])
            STATE = [[x],[y]]
            newvehi = Rot * vehi + STATE
            img = plt.plot(X,Y,marker=".",color="#FAAC58") + plt.plot(newvehi[0,:],newvehi[1,:],marker="p",color="#FAAC58")

            plt.title("FF")
            #plt.title("V = {}m/s".format(V[index]))
            #print("V = {}m/s".format(V[index]))
            #plt.title("V = "+ str(V[index])[:4])
            plt.axis("equal")
            plt.grid(True)
            ims.append(img)
        plt.pause(1)
        ani = animation.ArtistAnimation(fig, ims, interval=1)
        ####
        ax = plt.axes()
        ############################     field     #############################
        ########################################################################
        sotowaku = patches.Rectangle(xy=(-13.3+0.5,-0.5), width=13.3, height=10, ec='#FAAC58',fill=False)
        ax.add_patch(sotowaku)
        forest = patches.Rectangle(xy=(-2.45+0.5,-0.5), width=2.45, height=8, ec='#FAAC58',fill=False)
        ax.add_patch(forest)
        bridge = patches.Rectangle(xy=(-1.725 +0.5, 6.5 -0.5), width=1, height=1.5, ec='#FAAC58',fill=False)
        ax.add_patch(bridge)
        bri1 = patches.Circle(xy=(-1.725 +0.5, 6.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri1)
        bri2 = patches.Circle(xy=(-1.725 +0.5, 6.5+1.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri2)


        d = patches.Circle(xy=(-1*(1.225+ssp[0]),2+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(d)
        e = patches.Circle(xy=(-1*(1.225+ssp[0]),3.5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(e)
        f = patches.Circle(xy=(-1*(1.225+ssp[0]),5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(f)
        ########################################################################
        ########################################################################
        #'''
        plt.show()
        plt.plot(X,Y)
        plt.show()
