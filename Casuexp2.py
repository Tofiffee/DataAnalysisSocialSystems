import pandas as pd
import os
import numpy as np
import math

path = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(os.path.join(path, 'data', 'OneBee', 'coords_deg26_run04_huberpi2_exp220505-091006-utc_chw398-261_bee01.csv'))
df_new = df.drop(df.index[0])
df_new.loc[len(df_new)+1] = 0
df_new.reset_index(inplace=True)

df['bee1_r+1'] = df_new['bee1_r']
df['bee1_p+1'] = df_new['bee1_p']

df['bee1_r+1'] = df['bee1_r+1']/22.35
df['bee1_r'] = df['bee1_r']/22.35

df['angle'] = abs(df['bee1_p+1'] - df['bee1_p']) * math.pi * 180

df['distancePerFrame'] = 2 * math.pi * df['bee1_r'] * (df['angle']/360) #+ 2 * math.pi * df['bee1_r+1'] * (df['angle']/360))/2  # 2 * pi * r * alpha/360

df['distancePerSec'] = df['distancePerFrame']/0.2

print(df.head(50))