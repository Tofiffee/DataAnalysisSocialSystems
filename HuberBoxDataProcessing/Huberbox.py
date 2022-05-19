import os

from ctypes.wintypes import tagRECT
from matplotlib.pyplot import axis, plot
import pandas as pd
import scipy.stats as stats

from OneBee import dfProcessingSingle
from TwoBees import dfProcessingTwo
from ThreeBees import dfProcessingThree
from HuberboxCalculations import *
from plotting_Huberbox import boxplotTime


def DataProcessing():
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

def CalcSocialTogether():
    np_array_two_26 = np.array([])
    np_array_two_36 = np.array([])
    np_array_three_26 = np.array([])
    np_array_three_36 = np.array([])

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '26Degree')):
        array = claculationsTwo26(filename)
        np_array_two_26 = np.hstack((np_array_two_26,array))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '36Degree')):
        array = claculationsTwo36(filename)
        np_array_two_36 = np.hstack((np_array_two_36, array))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '26Degree')):
        array = claculationsThree26(filename)
        np_array_three_26 = np.hstack((np_array_three_26,array))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '36Degree')):
        array = claculationsThree36(filename)
        np_array_three_36 = np.hstack((np_array_three_36, array))

    return np_array_two_26, np_array_two_36, np_array_three_26, np_array_three_36

def main():
    DataProcessing()
    np_array_two_26, np_array_two_36, np_array_three_26, np_array_three_36 = CalcSocialTogether()

    plot1 = [np_array_two_26, np_array_three_26]
    plot2 = [np_array_two_36, np_array_three_36]
    x_axis = np.arange(len(plot1))
    labels = ['twoBees', 'threeBees']
    
    boxplotTime(plot1, plot2, x_axis=x_axis, label=labels)
    for i in [
        (np_array_two_26, np_array_two_36), 
        (np_array_two_26, np_array_three_26), 
        (np_array_two_26, np_array_three_36), 
        (np_array_three_26, np_array_three_36)
        ]:
        W, p = stats.mannwhitneyu(i[0], i[1], use_continuity=True, alternative='less')
        print(p)


if __name__ == '__main__':
    main()
