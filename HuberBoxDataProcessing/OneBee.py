import os

import pandas as pd
import math
import numpy as np

pxtocm = 22.35

def dfProcessingSingle(filename: str, number, deg):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'OneBee', filename))
    
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

    df['distancePerFrame'] = ((2 * math.pi * df['bee1_r'] * (df['angleGrad']/360)) + (2 * math.pi * df['bee1_r+1'] * 
    (df['angleGrad']/360)))/2

    df['distancePerSec'] = df['distancePerFrame']/0.2

    df['BeeNotMove'] = df['distancePerSec'].apply(lambda x: 1 if x <= 0.35 else 0)
    df = df[:-1]

    filename = filename.split('.')[0]

    df.to_csv(os.path.join(
        os.path.dirname(path), 'data', 'processedData', 'OneBee', f'{deg}', f'{filename}_processed_{number}.csv'
        ),
        sep=';',
        encoding='utf-8'
        )