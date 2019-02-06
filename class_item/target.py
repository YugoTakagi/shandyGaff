from class_item.target_item.bezier import bezier
from class_item.target_item.accel_designer import accel_designer
from class_item.target_item.integrate_number import integrate_number

#from color_class import pycolor as pc
import numpy as np
import math
import matplotlib.pyplot as plt
import csv


class target(object):
    """docstring for target"""
    dt = 0
    def __init__(self, dt):
        self.dt = dt
    def target_make(self, a, VEL, BEZIER, x_start, time_start, num):
        ##init##################################################################
        acd = accel_designer(self.dt)
        inb = integrate_number()
        bz = bezier(number_of_points=1000)

        X=[]

        NBEZIER = []
        NX = []
        NA = []
        NV = []
        NXX= []
        time = time_start
        length = x_start
        ######################     making X REF     ############################
        for i in range(num):
            npBEZIER = np.array(BEZIER[i])
            X.append([npBEZIER.T[0], npBEZIER.T[1], length])                    #X := [x_ref, y_ref, s_start]
            #print("X[{}] = {}".format(i, X[i]))
            A, V, XX, curve_length, t = acd.making_accel(a[i], VEL[i], X[i], time)
            print("{}> making accel fin".format(i))
            NBEZIER.extend(BEZIER[i])
            NA.extend(A)
            NV.extend(V)
            NXX.extend(XX)
            time += t
            length += curve_length
        npNBEZIER = np.array(NBEZIER)
        NX = [npNBEZIER.T[0], npNBEZIER.T[1], x_start]
        IN_INDEX, len_in_index = inb.integrate(NX, NXX)
        npREF, REF = bz.new_bezier_plt(NBEZIER, IN_INDEX, len_in_index)
        ######################     making V REF     ############################
        alfa = self.making_angle(npREF,len(npREF))
        vx, vy= self.making_vx_and_vy(NV,alfa,len(npREF))
        self.vx = vx
        self.vy = vy
        self.alfa = alfa

        plt.plot(NA, color ="red", marker="o", label='A')#marker=".", ls=""
        plt.plot(NV, color ="#FE9A2E", marker="o", label='V')#linewidth=3
        plt.plot(NXX, color ="Green", marker="o", label='X')
        plt.title("accel_designer")
        plt.legend()
        plt.show()
        print("> target fin\n")
        #return npBEZIER, BEZIER, npREF, REF, t, curve_length, vx, vy, alfa
        return REF, time, length, vx, vy, alfa

        '''
        npBEZIER = np.array(BEZIER)
        ######################     making X REF     ############################
        X = [npBEZIER.T[0], npBEZIER.T[1], x_start]
        A, V, XX, curve_length, t = acd.making_accel(a, VEL, X, time_start)
        IN_INDEX, len_in_index = inb.integrate(X, XX)
        npREF, REF = bz.new_bezier_plt(BEZIER, IN_INDEX, len_in_index)

        ######################     making V REF     ############################
        alfa = self.making_angle(npREF,len(npREF))
        vx, vy= self.making_vx_and_vy(V,alfa,len(npREF))
        self.vx = vx
        self.vy = vy
        self.alfa = alfa
        print("3> target fin\n")
        #return npBEZIER, BEZIER, npREF, REF, t, curve_length, vx, vy, alfa
        return REF, t, curve_length, vx, vy, alfa
        '''
    def making_vx_and_vy(self,V,ALFA,len):
        vx = []
        vy = []
        for index in np.arange(start=0, stop=len, step=1, dtype= int):#linspace_time:
            vx.append(V[index] * np.sin(ALFA[index]))
            vy.append(V[index] * np.cos(ALFA[index]))
        return vx, vy
    def making_angle(self, npREF, len_new_index_for_bezier):
        alfa=[]
        x_ref = npREF.T[0]
        y_ref = npREF.T[1]
        for index in np.arange(start=0, stop=len_new_index_for_bezier, step=1, dtype= int):
            if (index - 1) <= 0:
                dx = x_ref[index]
                dy = y_ref[index]
                pass
            else:
                dx = x_ref[index] - x_ref[index-1]
                dy = y_ref[index] - y_ref[index-1]
            alfa.append(math.atan2(dx, dy))
        ########################################################################
        '''
        BAT = []
        for index in np.arange(start=0, stop=len(alfa), step=1, dtype= int):
            if index-1 <0:
                pass
            else:
                if abs(alfa[index] -alfa[index -1]) >=np.pi/20:
                    BAT.append(index)
                    print("index", index)
                else:
                    pass
        for index in np.arange(start=0, stop=len(BAT), step=1, dtype= int):
            alfa[BAT[index]] = alfa[BAT[index] -1]
        '''
        return alfa
