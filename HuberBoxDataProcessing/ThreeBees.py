import os

import pandas as pd
import math

pxtocm = 22.35

def dfProcessingThree(filename: str, number, deg):
    '''
    Read in the data from the folder ThreeBees and converts them to calcualte the speed per second of the individual bees
    '''
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'ThreeBees', filename))
    
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

    df['angleGrad1'] = abs(df['bee1_p+1'] - df['bee1_p']) * (180/math.pi)
    df['angleGrad2'] = abs(df['bee2_p+1'] - df['bee2_p']) * (180/math.pi)
    df['angleGrad3'] = abs(df['bee3_p+1'] - df['bee3_p']) * (180/math.pi)

    df['angleDistance1_2'] = df.apply(lambda x: calcDistanceAngle(x['bee1_p'], x['bee2_p']), axis=1)
    df['angleDistGrad1_2'] = df['angleDistance1_2'].apply(lambda x: x * (180/math.pi))

    df['angleDistance1_3'] = df.apply(lambda x: calcDistanceAngle(x['bee1_p'], x['bee3_p']), axis=1)
    df['angleDistGrad1_3'] = df['angleDistance1_3'].apply(lambda x: x * (180/math.pi))

    df['angleDistance2_3'] = df.apply(lambda x: calcDistanceAngle(x['bee2_p'], x['bee3_p']), axis=1)
    df['angleDistGrad2_3'] = df['angleDistance2_3'].apply(lambda x: x * (180/math.pi))

    df['distancePerSec1'] = (((2 * math.pi * df['bee1_r'] * (df['angleGrad1']/360)) + (2 * math.pi * df['bee1_r+1'] * 
    (df['angleGrad1']/360)))/2)/0.2
    df['distancePerSec2'] = (((2 * math.pi * df['bee2_r'] * (df['angleGrad2']/360)) + (2 * math.pi * df['bee2_r+1'] * 
    (df['angleGrad2']/360)))/2)/0.2
    df['distancePerSec3'] = (((2 * math.pi * df['bee3_r'] * (df['angleGrad3']/360)) + (2 * math.pi * df['bee3_r+1'] * 
    (df['angleGrad3']/360)))/2)/0.2

    df['meanSpeed'] = (df['distancePerSec1'] + df['distancePerSec2'] + df['distancePerSec3'])/3

    df['distBees1_2'] = ((2 * math.pi * df['bee1_r'] * (df['angleDistGrad1_2']/360)) + (2 * math.pi * df['bee2_r'] * (df['angleDistGrad1_2']/360)))/2
    df['distBees1_3'] = ((2 * math.pi * df['bee1_r'] * (df['angleDistGrad1_3']/360)) + (2 * math.pi * df['bee3_r'] * (df['angleDistGrad1_3']/360)))/2
    df['distBees2_3'] = ((2 * math.pi * df['bee2_r'] * (df['angleDistGrad2_3']/360)) + (2 * math.pi * df['bee3_r'] * (df['angleDistGrad2_3']/360)))/2
    
    df['BeesClose1_2'] = df['distBees1_2'].apply(lambda x: 1 if x <= 2.2 else 0)
    df['BeesClose1_3'] = df['distBees1_3'].apply(lambda x: 1 if x <= 2.2 else 0)
    df['BeesClose2_3'] = df['distBees2_3'].apply(lambda x: 1 if x <= 2.2 else 0)

    df['BeeNotMove1'] = df['distancePerSec1'].apply(lambda x: 1 if x <= 0.35 else 0)
    df['BeeNotMove2'] = df['distancePerSec2'].apply(lambda x: 1 if x <= 0.35 else 0)
    df['BeeNotMove3'] = df['distancePerSec3'].apply(lambda x: 1 if x <= 0.35 else 0)

    df['meanDist'] = (df['distBees1_2'] + df['distBees1_3'] + df['distBees2_3'])/3
    df['BeesClose1_2_3'] = df['meanDist'].apply(lambda x: 1 if x <= 2.2 else 0)

    df = df[:-1]

    df.to_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees',  f'{deg}', f'{filename}_processed_{number}.csv'),
    sep=';', encoding='utf-8')

def calcDistanceAngle(rad1, rad2):
        angle = abs(rad2 - rad1)

        if angle > math.pi:
            return (2*math.pi) - angle
        elif angle < math.pi:
            return angle