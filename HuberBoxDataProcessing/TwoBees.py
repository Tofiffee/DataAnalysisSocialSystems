import os

import pandas as pd
import math
import numpy as np

pxtocm = 22.35

def dfProcessingTwo(filename: str, number, deg):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'TwoBees', filename))

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

    df['angleGrad1'] = abs(df['bee1_p+1'] - df['bee1_p']) * (180/math.pi)
    df['angleGrad2'] = abs(df['bee2_p+1'] - df['bee2_p']) * (180/math.pi)

    df['angleDistance'] = df.apply(lambda x: calcDistanceAngle(x['bee1_p'], x['bee2_p']), axis=1)
    df['angleDistGrad'] = df['angleDistance'].apply(lambda x: x * (180/math.pi))

    df['distancePerSec1'] = (((2 * math.pi * df['bee1_r'] * (df['angleGrad1']/360)) + (2 * math.pi * df['bee1_r+1'] * 
    (df['angleGrad1']/360)))/2)/0.2
    df['distancePerSec2'] = (((2 * math.pi * df['bee2_r'] * (df['angleGrad2']/360)) + (2 * math.pi * df['bee2_r+1'] * 
    (df['angleGrad2']/360)))/2)/0.2

    df['distBees'] = ((2 * math.pi * df['bee1_r'] * (df['angleDistGrad']/360)) + (2 * math.pi * df['bee2_r'] * 
    (df['angleDistGrad']/360)))/2

    df['BeeNotMove1'] = df['distancePerSec1'].apply(lambda x: 1 if x <= 0.35 else 0)
    df['BeeNotMove2'] = df['distancePerSec2'].apply(lambda x: 1 if x <= 0.35 else 0)
    df['meanSpeed'] = (df['distancePerSec1'] + df['distancePerSec2'])/2

    df['BeesClose'] = df['distBees'].apply(lambda x: 1 if x <=2.2 else 0)
    
    df = df[:-1]

    df.to_csv(os.path.join(
        os.path.dirname(path), 'data', 'processedData', 'TwoBees',  f'{deg}', f'{filename}_processed_{number}.csv'
        ), 
        sep=';', encoding='utf-8') 

def calcDistanceAngle(rad1, rad2):
        angle = abs(rad2 - rad1)

        if angle > math.pi:
            return (2*math.pi) - angle
        elif angle < math.pi:
            return angle