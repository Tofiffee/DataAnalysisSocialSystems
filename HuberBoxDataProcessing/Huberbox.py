import os

from ctypes.wintypes import tagRECT
from matplotlib.pyplot import axis, plot
import pandas as pd
import scipy.stats as stats

from OneBee import dfProcessingSingle
from TwoBees import dfProcessingTwo
from ThreeBees import dfProcessingThree
from HuberboxCalculationsTime import *
from plotting_Huberbox import boxplot
from HuberboxCalculationsSpeed import *


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

def CalcSpeed():
    path = os.path.dirname(os.path.realpath(__file__))

    speedOne26array = np.array([])
    speedOne36array = np.array([])
    speedTwo26array = np.array([])
    speedTwo36array = np.array([])
    speedThree26array = np.array([])
    speedThree36array = np.array([])

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'OneBee', '26Degree')):
        speedValues = speedOne26(filename)
        speedOne26array = np.hstack((speedOne26array, speedValues))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'OneBee', '36Degree')):
        speedValues = speedOne36(filename)
        speedOne36array = np.hstack((speedOne36array, speedValues))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '26Degree')):
        speedValues = speedTwo26(filename)
        speedTwo26array = np.hstack((speedTwo26array, speedValues))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '36Degree')):
        speedValues = speedTwo36(filename)
        speedTwo36array = np.hstack((speedTwo36array, speedValues))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '26Degree')):
        speedValues = speedThree26(filename)
        speedThree26array = np.hstack((speedThree26array, speedValues))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '36Degree')):
        speedValues = speedThree36(filename)
        speedThree36array = np.hstack((speedThree36array, speedValues))
 
    return speedOne26array, speedOne36array, speedTwo26array, speedTwo36array, speedThree26array, speedThree36array
        


def main():
    DataProcessing()
    np_array_two_26, np_array_two_36, np_array_three_26, np_array_three_36 = CalcSocialTogether()
    speedOne26array, speedOne36array, speedTwo26array, speedTwo36array, speedThree26array, speedThree36array = CalcSpeed()

    plotA1 = [np_array_two_26, np_array_three_26]
    plotA2 = [np_array_two_36, np_array_three_36]
    plotB1 = [speedOne26array, speedTwo26array, speedThree26array]
    plotB2 = [speedOne36array, speedTwo36array, speedThree36array]
    x_axis_A = np.arange(len(plotA1))
    x_axis_B = np.arange(len(plotB1))
    labels_A = ['twoBees', 'threeBees']
    labels_B = ['oneBee', 'twoBees', 'threeBees']
    
    boxplot(
        listA1=plotA1, listA2=plotA2, x_axis_A=x_axis_A, label_A=labels_A,
        listB1=plotB1, listB2=plotB2, x_axis_B=x_axis_B, label_B=labels_B
        )
        
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
