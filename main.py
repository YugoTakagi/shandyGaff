from game import game

import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    ##########################  init controler  ################################
    gm = game(0.008)
    ############################################################################

    #gm.run(False)
    #gm.run(True)
    #gm.run_line(True)
    #gm.run_cal(False)
    #gm.run_cal(True)
    #gm.run_calab(False)
    #gm.run_calab(True)
    #gm.run_cal2(False)
    gm.runCalBlue(False)
    #gm.runWayBlue(False)
if __name__ == '__main__':
    print("++++    +++   ++  + start main +  ++   +++    ++++")
    main()
    print("++++    +++   ++  + end main +  ++   +++    ++++")
