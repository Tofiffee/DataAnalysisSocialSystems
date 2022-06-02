import os

import scipy.stats as stats
import numpy as np

from HuberboxCalculationsTime import *
from plotting_Huberbox import boxplot
from HuberboxCalculationsSpeed import *

def CalcSocialTogether() ->  np.ndarray:
    """calculates all the social times for all the files in the direcories in the folder processed data

    Returns:
        np.ndarray: returns the times for social interaction for one, two and three bees for 26 and 36 degrees
    """
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

def CalcSpeed() -> np.ndarray:
    """calcualtes the speeds for all the files in the directories in the folder processed data

    Returns:
        np.ndarray: the speed values for one, two and three bees at 26 and 36 degrees
    """
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
        print(speedValues)

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
