import os

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

from plottingCasu2 import BoxplotCasu2

def ReadData(url: str) -> pd.DataFrame: 
    """    This function downloads the data from a GoogleTable sheet with the given link and transformes them into a csv and then reads them in into a pd.DataFrame

    Args:
        url (str): The URL of the datasheet were the data is stored on the GoogleDrive, the sheet needs to be shared via
        link with the seeting that everybody with this link can edit. The Link you need for this function is the URL of 
        the datasheet in the browser.

    Returns:
        pd.DataFrame: Returns a pandas DataFrame with the data from the first sheet for the GoogleTable spreedsheet
    """
    url_read = url.replace('/edit#gid=', '/export?format=csv&gid=')

    df = pd.read_csv(url_read, on_bad_lines='skip')

    return df

def dfProcessing(df, beeNumber, keyword1, keyword2):
    array1 = np.array([])
    array2 = np.array([])

    for column in df.columns.values.tolist()[1:]:
        df[f'{column}'] = df[f'{column}'].apply(lambda x: x/beeNumber*100)
        if keyword1 in column:
            array = df[f'{column}'].to_numpy()
            array1 = np.hstack((array1, array))
        elif keyword2 in column:
            array = df[f'{column}'].to_numpy()
            array2 = np.hstack((array2, array))

    return array1, array2

df = ReadData('https://docs.google.com/spreadsheets/d/1c5eXRyP4uLSDKJ_1PHlx48nZ8wQ06mUr1Ayrty-kfDg/edit#gid=0')
df_controlTemp = ReadData('https://docs.google.com/spreadsheets/d/1rtl7NfzKXGVWi90JLlAunum5BX6TK17NUiaficQs9q0/edit#gid=0')
df_controlNoTemp = ReadData('https://docs.google.com/spreadsheets/d/1IzRJBgdS33K6GxaT-alZ26ywCZD9hzXSLbW1mHwKXsA/edit#gid=0')

Temp, Bees = dfProcessing(df, 6, 'Temp', 'Bienen')
Temp_cont, noTemp_cont = dfProcessing(df_controlTemp, 5, 'CasuT', 'CasunT')
noTemp1_cont, noTemp2_cont = dfProcessing(df_controlNoTemp, 5, 'Casu1', 'Casu2')

plot1 = [noTemp2_cont, noTemp_cont, Bees]
plot2 = [noTemp1_cont, Temp_cont, Temp]

statistic1, p_shapiro1 = stats.shapiro(noTemp1_cont)
statistic2, p_ks1 = stats.kstest(noTemp1_cont, 'norm', mode='exact')
statistic3, p_shapiro2 = stats.shapiro(noTemp2_cont)
statistic4, p_ks2 = stats.kstest(noTemp2_cont, 'norm', mode='exact')

statistic5, p_val = stats.mannwhitneyu(noTemp1_cont, noTemp2_cont, use_continuity=True, alternative='less')


print(p_shapiro1, p_ks1)
print(p_shapiro2, p_ks2)
print(p_val)

labels = ['control', 'empty vs Temp', 'Bees vs Temp']
path = os.path.realpath(os.path.dirname(__file__))
path = os.path.join(path, '..', 'graphs')

BoxplotCasu2(plot1, plot2, labels, path)
