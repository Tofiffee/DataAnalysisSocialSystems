import os

import pandas as pd
import math

pxtocm = 22.35 #Factor for transformation from pixel distance to cm

def dfProcessingSingle(filename: str, number: int, deg: str) -> pd.DataFrame:
    """This function calcualtes from basedate (csv_file which is read in into a pd.DataFrame) the distance that a bee walks per frame, the distance the bee walks per second, If the bee moves. It return a pandas df wich is saved as a csv file in the directory given at the end of the function

    Args:
        filename (str): The filename that needs to be processed in the given directory
        number (int): a unique number (should be generated by a counter) that gives all the datanames uniquness
        deg (str): The degrees with which the experiments were performed (to find the right dataset and to write it into the right directory either 26Degree or 36Degree)

    Returns:
        pd.DataFrame: DataFrame is saves as csv file into the direcoty path/data/processedData/OneBee/deg/
    """
    path = os.path.dirname(os.path.realpath(__file__)) #generates path to this file

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'OneBee', filename)) #reads in basedata from given directory
    
    df_new = df.drop(df.index[0]) #creates a new dataframe were the first line gets deleted
    df_new.loc[len(df_new)+1] = 0 #sets the last line of the new dataframe to zero in all columns
    df_new.reset_index(inplace=True) #resets the index of the new dataframe

    # writes the two columns from the new dataframe to the old dataframe
    df['bee1_r+1'] = df_new['bee1_r']
    df['bee1_p+1'] = df_new['bee1_p']

    # transforms radius data form pixels to cm
    df['bee1_r+1'] = df['bee1_r+1']/pxtocm
    df['bee1_r'] = df['bee1_r']/pxtocm
    
    # calculates angle that the bee moves in one timestep and transformes rad to grad
    df['angleGrad'] = abs(df['bee1_p+1'] - df['bee1_p']) * (180/math.pi)
    # If angle is over 180 degrees it resets to the smaller angle
    df['angleGrad'] = df['angleGrad'].apply(lambda x: 360-x if x > 180 else x)

    # calculates the distance per frame with the mean of the two radiuses of the time n and n+1
    df['distancePerFrame'] = ((2 * math.pi * df['bee1_r'] * (df['angleGrad']/360)) + (2 * math.pi * df['bee1_r+1'] * 
    (df['angleGrad']/360)))/2
    df['distancePerSec'] = df['distancePerFrame']/0.2

    # sets the threshold for not moving
    df['BeeNotMove'] = df['distancePerSec'].apply(lambda x: 1 if x <= 0.35 else 0)
    df['distancePerSec'] = df['distancePerSec'].apply(lambda x: 0 if x <= 0.35 else x)
    df = df[:-1]

    filename = filename.split('.')[0]

    # writes the datafile to a csv file
    df.to_csv(os.path.join(
        os.path.dirname(path), 'data', 'processedData', 'OneBee', f'{deg}', f'{filename}_processed_{number}.csv'
        ),
        sep=';',
        encoding='utf-8'
        )