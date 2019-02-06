from game import game

import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    ##########################  init controler  ################################
    gm = game(0.020)
    ############################################################################

    #gm.run(False)
    #gm.run(True)
    #gm.run_line(True)
    #gm.run_cal(False)
    gm.run_cal(True)
if __name__ == '__main__':
    print("++++    +++   ++  + start main +  ++   +++    ++++")
    main()
    print("++++    +++   ++  + end main +  ++   +++    ++++")
