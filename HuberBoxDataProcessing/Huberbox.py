import os

import scipy.stats as stats
import numpy as np

from HuberboxCalculationsTime import *
from plotting_Huberbox import boxplot
from HuberboxCalculationsSpeed import *
from statisticsPipline import StatisticalTesting

def CalcSocialTogether() ->  np.ndarray:
    """calculates all the social times for all the files in the direcories in the folder processed data

    Returns:
        np.ndarray: returns the times for social interaction for one, two and three bees for 26 and 36 degrees
    """
    np_array_two_26 = np.array([])
    np_array_two_36 = np.array([])
    np_array_three_26_Two = np.array([])
    np_array_three_36_Two = np.array([])
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

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '26Degree')):
        array = claculationsThree26Two(filename)
        np_array_three_26_Two = np.hstack((np_array_three_26_Two, array))

    for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '36Degree')):
        array = claculationsThree36Two(filename)
        np_array_three_36_Two = np.hstack((np_array_three_36_Two, array))

    return np_array_two_26, np_array_two_36, np_array_three_26_Two, np_array_three_36_Two, np_array_three_26, np_array_three_36

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
    np_array_two_26, np_array_two_36, np_array_three_26_Two, np_array_three_36_Two, np_array_three_26, np_array_three_36 = CalcSocialTogether()
    speedOne26array, speedOne36array, speedTwo26array, speedTwo36array, speedThree26array, speedThree36array = CalcSpeed()

    TestData = [
        {'Data1': np_array_two_26, 'Data2': np_array_two_36, 'alternativ': 'less', 'dependent': False},
        {'Data1': np_array_three_26_Two, 'Data2': np_array_three_36_Two, 'alternativ': 'less', 'dependent': False},
        {'Data1': np_array_two_26, 'Data2': np_array_three_26_Two, 'alternativ': 'less', 'dependent': False},
        {'Data1': np_array_two_36, 'Data2': np_array_three_36_Two, 'alternativ': 'less', 'dependent': False},
        {'Data1': np_array_three_36_Two, 'Data2': np_array_three_36, 'alternativ': 'less', 'dependent': False},
        {'Data1': np_array_three_26_Two, 'Data2': np_array_three_36, 'alternativ': 'less', 'dependent': False}
        ]

    for i in TestData:
        result = StatisticalTesting(i)
        print(result)

    statistic, p_anova26 = stats.f_oneway(speedOne26array, speedTwo26array, speedThree26array)
    statistic, p_anova36 = stats.f_oneway(speedOne36array, speedTwo36array, speedThree36array)

    print(f'The anova for 26 degrees shows a p_value of {p_anova26}')
    print(f'The anova for 36 degrees shows a p_value of {p_anova36}')

    plotA1 = [np_array_two_26, np_array_three_26_Two, np_array_three_26]
    plotA2 = [np_array_two_36,np_array_three_36_Two, np_array_three_36]
    plotB1 = [speedOne26array, speedTwo26array, speedThree26array]
    plotB2 = [speedOne36array, speedTwo36array, speedThree36array]
    x_axis_A = np.arange(len(plotA1))
    x_axis_B = np.arange(len(plotB1))
    labels_A = ['two Bees', 'two out of three', 'three Bees']
    labels_B = ['one Bee', 'two Bees', 'three Bees']
    
    boxplot(
        listA1=plotA1, listA2=plotA2, x_axis_A=x_axis_A, label_A=labels_A,
        listB1=plotB1, listB2=plotB2, x_axis_B=x_axis_B, label_B=labels_B
        )

if __name__ == '__main__':
    main()
