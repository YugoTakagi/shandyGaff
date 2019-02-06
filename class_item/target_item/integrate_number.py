import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class integrate_number(object):
    """docstring for arrange_the_point."""
    maxmum_interval = 0
    minmumInterval = 0
    def __init__(self):
        pass
    def integrate(self, X, TVP_of_S):
        #print('----------start integrate number-----------')
        ARRANGE_INDEXS = []
        sum_s = 0.0
        index_of_tvp = 0
        ds_befor=0

        before_x = X[0]
        before_y = X[1]
        x_start  = X[2]
        for index in np.arange(0, len(before_x), 1):
            if (index-1) < 0:
                #dx = before_x[index]
                #dy = before_y[index]
                #ds = np.sqrt(dx**2 + dy**2)
                ds = x_start
            else:
                dx = before_x[index] - before_x[index-1]
                dy = before_y[index] - before_y[index-1]
                ds = np.sqrt(dx**2 + dy**2)
            sum_s = sum_s + ds
            ds_befor = ds
            if sum_s >= TVP_of_S[index_of_tvp]:
                #print("sum[{}] , s[{}] = {} , {}".format(index, index_of_tvp, sum_s, TVP_of_S[index_of_tvp]))
                ARRANGE_INDEXS.append(index)
                index_of_tvp += 1
                if len(ARRANGE_INDEXS) == len(TVP_of_S):
                    print("> integrate fin")
                    break
        print(">> integrate({}): {} -> {}".format(len(TVP_of_S),len(before_x),len(ARRANGE_INDEXS)))
        #print('-------------------------------------------')
        return ARRANGE_INDEXS, len(ARRANGE_INDEXS)
    def maximumInterval(self, TVP_of_S):
        INDEX_OF_TVPS = np.arange(start=0.0, stop=len(TVP_of_S)-1, step=1, dtype= int)
        for index in INDEX_OF_TVPS:
            if (index-1) <= 0:
                self.maxmum_interval = TVP_of_S[index]
            else:
                interval = TVP_of_S[index] - TVP_of_S[index-1]
                if self.maxmum_interval<interval:
                    self.maxmum_interval = interval
                else:
                    pass
        print('self.maxmum_interval = {}'.format(self.maxmum_interval))
    def minmumInterval(self, TVP_of_S):
        INDEX_OF_TVPS = np.arange(start=0.0, stop=len(TVP_of_S)-1, step=1, dtype= int)
        for index in INDEX_OF_TVPS:
            if (index-1) <= 0:
                self.minmum_interval = TVP_of_S[index]
            else:
                interval = TVP_of_S[index] - TVP_of_S[index-1]
                if self.minmum_interval>interval:
                    self.minmum_interval = interval
                else:
                    pass
        print('self.minmum_interval = {}'.format(self.minmum_interval))
