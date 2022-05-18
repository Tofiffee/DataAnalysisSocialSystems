import os

from ctypes.wintypes import tagRECT
from matplotlib.pyplot import axis, plot
import pandas as pd
import scipy.stats as stats

from OneBee import dfProcessingSingle
from TwoBees import dfProcessingTwo
from ThreeBees import dfProcessingThree


pxtocm = 22.35

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    number = 0

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'OneBee')):
        number += 1
        if 'deg26' in filename:
            dfProcessingSingle(filename, number, '26Degree')
        elif 'deg36' in filename:
            dfProcessingSingle(filename, number, '36Degree')

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'TwoBees')):
        number += 1
        if 'deg26' in filename:
            dfProcessingTwo(filename, number, '26Degree')
        elif 'deg36' in filename:
            dfProcessingTwo(filename, number, '36Degree')

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'ThreeBees')):
        number += 1
        if 'deg26' in filename:
            dfProcessingThree(filename, number, '26Degree')
        elif 'deg36' in filename:
            dfProcessingThree(filename, number, '36Degree')


if __name__ == '__main__':
    main()
