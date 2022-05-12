from matplotlib.pyplot import plot
import pandas as pd
import os
import numpy as np
import math

from plotting_Huberbox import plot_speed_single

def dfProcessingSingle(filename):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(path, 'data', 'OneBee', filename))
    
    df_new = df.drop(df.index[0])
    df_new.loc[len(df_new)+1] = 0
    df_new.reset_index(inplace=True)

    df['bee1_r+1'] = df_new['bee1_r']
    df['bee1_p+1'] = df_new['bee1_p']

    df['bee1_r+1'] = df['bee1_r+1']/22.35
    df['bee1_r'] = df['bee1_r']/22.35

    df['distancePerFrame'] = ((2 * math.pi * df['bee1_r'] * (df['bee1_p']/360)) + (2 * math.pi * df['bee1_r+1'] * (df['bee1_p+1']/360)))/2

    df['distancePerSec'] = df['distancePerFrame']/0.2

    df['distancePerSec'] = df['distancePerSec'].apply(lambda x: 0 if x <= 0.35 else x)
    df = df[:-1]

    return df

def dfProcessingThree(filename):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(path, 'data', 'ThreeBees', filename))
    
    df_new = df.drop(df.index[0])
    df_new.loc[len(df_new)+1] = 0
    df_new.reset_index(inplace=True)

    # df['bee1_r+1'] = df_new['bee1_r']
    # df['bee1_p+1'] = df_new['bee1_p']

    # df['bee1_r+1'] = df['bee1_r+1']/22.35
    # df['bee1_r'] = df['bee1_r']/22.35

    # df['distancePerFrame'] = ((2 * math.pi * df['bee1_r'] * (df['bee1_p']/360)) + (2 * math.pi * df['bee1_r+1'] * (df['bee1_p+1']/360)))/2

    # df['distancePerSec'] = df['distancePerFrame']/0.2

    # df['distancePerSec'] = df['distancePerSec'].apply(lambda x: 0 if x <= 0.35 else x)
    # df = df[:-1]

    return df

def main():
    path = os.path.dirname(os.path.realpath(__file__))

    list_26 = []
    list_36 = []

    for filename in os.listdir(os.path.join(path, 'data', 'OneBee')):
        if 'deg26' in filename:
            df = dfProcessingSingle(filename)
            list_26.append(df)
        elif 'deg36' in filename:
            df = dfProcessingSingle(filename)
            list_36.append(df)
    
    
    plot_speed_single(list_26[0]['second'], list_26, 'plot_26.png')
    plot_speed_single(list_36[0]['second'], list_36, 'plot_36.png')

if __name__ == '__main__':
    main()
