from ctypes.wintypes import tagRECT
from matplotlib.pyplot import axis, plot
import pandas as pd
import os
import numpy as np
import math
import scipy.stats as stats

pxtocm = 22.35

from plotting_Huberbox import plot_speed_single

def dfProcessingSingle(filename: str, number):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(path, 'data', 'OneBee', filename))
    
    df_new = df.drop(df.index[0])
    df_new.loc[len(df_new)+1] = 0
    df_new.reset_index(inplace=True)

    df['bee1_r+1'] = df_new['bee1_r']
    df['bee1_p+1'] = df_new['bee1_p']

    df['bee1_r+1'] = df['bee1_r+1']/pxtocm
    df['bee1_r'] = df['bee1_r']/pxtocm
    df['angleGrad'] = abs(df['bee1_p+1'] - df['bee1_p']) * (180/math.pi)
    
    df.drop(df.tail(1).index, inplace=True)
    df['angleGrad'] = df['angleGrad'].apply(lambda x: 360 - x if x > 200 else x)

    df['distancePerFrame'] = ((2 * math.pi * df['bee1_r'] * (df['angleGrad']/360)) + (2 * math.pi * df['bee1_r+1'] * (df['angleGrad']/360)))/2

    df['distancePerSec'] = df['distancePerFrame']/0.2

    df['distancePerSec'] = df['distancePerSec'].apply(lambda x: 0 if x <= 0.35 else x)
    df = df[:-1]

    df.to_csv(os.path.join(path, 'data', 'processedData', 'OneBee', f'{filename}_processed_{number}'))  

def dfProcessingTwo(filename: str, number):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(path, 'data', 'TwoBees', filename))
    
    df_new = df.drop(df.index[0])
    df_new.loc[len(df_new)+1] = 0
    df_new.reset_index(inplace=True)

    df['bee1_r+1'] = df_new['bee1_r']
    df['bee2_r+1'] = df_new['bee2_r']

    df['bee1_p+1'] = df_new['bee1_p']
    df['bee2_p+1'] = df_new['bee2_p']

    df['bee1_r+1'] = df['bee1_r+1']/pxtocm
    df['bee1_r'] = df['bee1_r']/pxtocm

    df['bee2_r+1'] = df['bee2_r+1']/pxtocm
    df['bee2_r'] = df['bee2_r']/pxtocm

    df.drop(df.tail(1).index, inplace=True)

    df['angleGrad1'] = abs(df['bee1_p+1'] - df['bee1_p']) * (180/math.pi)
    df['angleGrad2'] = abs(df['bee2_p+1'] - df['bee2_p']) * (180/math.pi)

    df['distancePerSec1'] = (((2 * math.pi * df['bee1_r'] * (df['angleGrad1']/360)) + (2 * math.pi * df['bee1_r+1'] * (df['angleGrad1']/360)))/2)/0.2
    df['distancePerSec2'] = (((2 * math.pi * df['bee2_r'] * (df['angleGrad2']/360)) + (2 * math.pi * df['bee2_r+1'] * (df['angleGrad2']/360)))/2)/0.2

    df['distancePerSec1'] = df['distancePerSec1'].apply(lambda x: 0 if x <= 0.35 else x)
    df['distancePerSec2'] = df['distancePerSec2'].apply(lambda x: 0 if x <= 0.35 else x)
    df['meanSpeed'] = (df['distancePerSec1'] + df['distancePerSec2'])/2

    df = df[:-1]

    df.to_csv(os.path.join(path, 'data', 'processedData', 'TwoBees', f'{filename}_processed_{number}'))  

def dfProcessingThree(filename: str, number):
    '''
    Read in the data from the folder ThreeBees and converts them to calcualte the speed per second of the individual bees
    '''
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(path, 'data', 'ThreeBees', filename))
    
    df_new = df.drop(df.index[0])
    df_new.loc[len(df_new)+1] = 0
    df_new.reset_index(inplace=True)

    df['bee1_r+1'] = df_new['bee1_r']
    df['bee2_r+1'] = df_new['bee2_r']
    df['bee3_r+1'] = df_new['bee3_r']

    df['bee1_p+1'] = df_new['bee1_p']
    df['bee2_p+1'] = df_new['bee2_p']
    df['bee3_p+1'] = df_new['bee3_p']

    df['bee1_r+1'] = df['bee1_r+1']/pxtocm
    df['bee1_r'] = df['bee1_r']/pxtocm

    df['bee2_r+1'] = df['bee2_r+1']/pxtocm
    df['bee2_r'] = df['bee2_r']/pxtocm

    df['bee3_r+1'] = df['bee3_r+1']/pxtocm
    df['bee3_r'] = df['bee3_r']/pxtocm

    df.drop(df.tail(1).index, inplace=True)

    df['angleGrad1'] = abs(df['bee1_p+1'] - df['bee1_p']) * (180/math.pi)
    df['angleGrad2'] = abs(df['bee2_p+1'] - df['bee2_p']) * (180/math.pi)
    df['angleGrad3'] = abs(df['bee3_p+1'] - df['bee3_p']) * (180/math.pi)

    df['distancePerSec1'] = (((2 * math.pi * df['bee1_r'] * (df['angleGrad1']/360)) + (2 * math.pi * df['bee1_r+1'] * (df['angleGrad1']/360)))/2)/0.2
    df['distancePerSec2'] = (((2 * math.pi * df['bee2_r'] * (df['angleGrad2']/360)) + (2 * math.pi * df['bee2_r+1'] * (df['angleGrad2']/360)))/2)/0.2
    df['distancePerSec3'] = (((2 * math.pi * df['bee3_r'] * (df['angleGrad3']/360)) + (2 * math.pi * df['bee3_r+1'] * (df['angleGrad3']/360)))/2)/0.2

    df['distancePerSec1'] = df['distancePerSec1'].apply(lambda x: 0 if x <= 0.35 else x)
    df['distancePerSec2'] = df['distancePerSec2'].apply(lambda x: 0 if x <= 0.35 else x)
    df['distancePerSec3'] = df['distancePerSec3'].apply(lambda x: 0 if x <= 0.35 else x)

    df['meanSpeed'] = (df['distancePerSec1'] + df['distancePerSec2'] + df['distancePerSec3'])/3

    df = df[:-1]

    df.to_csv(os.path.join(path, 'data', 'processedData', 'ThreeBees', f'{filename}_prcessing_{number}'))  

def calcDistanceAngle(rad1, rad2):
    angle = abs(rad2 - rad1)

    if angle > math.pi:
        return (2*math.pi) - angle
    elif angle < math.pi:
        return angle

def distanceTwo(filename, number):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(path, 'data', 'TwoBees', filename))

    df['angleDistance'] = df.apply(lambda x: calcDistanceAngle(x['bee1_p'], x['bee2_p']), axis=1)
    df['angleDistGrad'] = df['angleDistance'].apply(lambda x: x * (180/math.pi))

    df['bee1_r'] = df['bee1_r']/pxtocm
    df['bee2_r'] = df['bee2_r']/pxtocm

    df['distBees'] = ((2 * math.pi * df['bee1_r'] * (df['angleDistGrad']/360)) + (2 * math.pi * df['bee2_r'] * (df['angleDistGrad']/360)))/2
    
    df.to_csv(os.path.join(path, 'data', 'processedData', 'TwoBees', f'{filename}_distance_{number}'))    


def distanceThree(filename, number):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(path, 'data', 'ThreeBees', filename))

    df['angleDistance1_2'] = df.apply(lambda x: calcDistanceAngle(x['bee1_p'], x['bee2_p']), axis=1)
    df['angleDistGrad1_2'] = df['angleDistance1_2'].apply(lambda x: x * (180/math.pi))

    df['angleDistance1_3'] = df.apply(lambda x: calcDistanceAngle(x['bee1_p'], x['bee3_p']), axis=1)
    df['angleDistGrad1_3'] = df['angleDistance1_3'].apply(lambda x: x * (180/math.pi))

    df['angleDistance2_3'] = df.apply(lambda x: calcDistanceAngle(x['bee2_p'], x['bee3_p']), axis=1)
    df['angleDistGrad2_3'] = df['angleDistance2_3'].apply(lambda x: x * (180/math.pi))

    df['bee1_r'] = df['bee1_r']/pxtocm
    df['bee2_r'] = df['bee2_r']/pxtocm
    df['bee3_r'] = df['bee3_r']/pxtocm

    df['distBees1_2'] = ((2 * math.pi * df['bee1_r'] * (df['angleDistGrad1_2']/360)) + (2 * math.pi * df['bee2_r'] * (df['angleDistGrad1_2']/360)))/2
    df['distBees1_3'] = ((2 * math.pi * df['bee1_r'] * (df['angleDistGrad1_3']/360)) + (2 * math.pi * df['bee3_r'] * (df['angleDistGrad1_3']/360)))/2
    df['distBees2_3'] = ((2 * math.pi * df['bee2_r'] * (df['angleDistGrad2_3']/360)) + (2 * math.pi * df['bee3_r'] * (df['angleDistGrad2_3']/360)))/2
    
    df['meanDist'] = (df['distBees1_2'] + df['distBees1_3'] + df['distBees2_3'])/3

    df.to_csv(os.path.join(path, 'data', 'processedData', 'ThreeBees', f'{filename}_distance_{number}'))

def main():
    path = os.path.dirname(os.path.realpath(__file__))

    list_one_speed_26 = []
    list_one_speed_36 = []

    list_two_speed_26 = []
    list_two_speed_36 = []
    list_two_dist_26 = []
    list_two_dist_36 = []

    list_three_speed_26 = []
    list_three_speed_36 = []
    list_three_dist_26 = []
    list_three_dist_36 = []

    number = 0

    for filename in os.listdir(os.path.join(path, 'data', 'OneBee')):
        number += 1
        print(number)
        if 'deg26' in filename:
            dfProcessingSingle(filename, number)
        elif 'deg36' in filename:
            dfProcessingSingle(filename, number)

    for filename in os.listdir(os.path.join(path, 'data', 'TwoBees')):
        number += 1
        if 'deg26' in filename:
            dfProcessingTwo(filename, number)
            distanceTwo(filename, number)
        elif 'deg36' in filename:
            dfProcessingTwo(filename, number)
            distanceTwo(filename, number)

    for filename in os.listdir(os.path.join(path, 'data', 'ThreeBees')):
        number += 1
        if 'deg26' in filename:
            dfProcessingThree(filename, number)
            distanceThree(filename, number)
        elif 'deg36' in filename:
            dfProcessingThree(filename, number)
            distanceThree(filename, number)

    lists = [list_one_speed_26, list_one_speed_36, list_two_speed_26, list_two_speed_36, list_three_speed_26, list_three_speed_36]

    for data in lists:
        W, p1 = stats.shapiro(data)
        D, p2 = stats.kstest(data, 'norm')
        print("Shapiro-Wilk: W:{0} p={1}".format(W, p1))
        print("Kolmogorov-Smirnov: D:{0} p={1}".format(D, p2))
        print(' ')

    print(stats.mannwhitneyu(list_one_speed_26, list_one_speed_36, use_continuity=True, alternative='less'))
    print(stats.mannwhitneyu(list_two_speed_26, list_two_speed_36, use_continuity=True, alternative='less'))
    print(stats.mannwhitneyu(list_three_speed_26, list_three_speed_36, use_continuity=True, alternative='less'))
    print(' ')
    print(stats.mannwhitneyu(list_one_speed_26, list_two_speed_26, use_continuity=True, alternative='less'))
    print(stats.mannwhitneyu(list_one_speed_26, list_three_speed_26, use_continuity=True, alternative='less'))
    print(stats.mannwhitneyu(list_two_speed_26, list_three_speed_26, use_continuity=True, alternative='less'))
    print(' ')
    print(stats.mannwhitneyu(list_one_speed_36, list_two_speed_36, use_continuity=True, alternative='less'))
    print(stats.mannwhitneyu(list_one_speed_36, list_three_speed_36, use_continuity=True, alternative='less'))
    print(stats.mannwhitneyu(list_two_speed_36, list_three_speed_36, use_continuity=True, alternative='less'))

    # plot_speed_single(list_one_26[0]['second'], list_one_26, 'plot_26.png')
    # plot_speed_single(list_one_36[0]['second'], list_one_36, 'plot_36.png')

if __name__ == '__main__':
    main()
