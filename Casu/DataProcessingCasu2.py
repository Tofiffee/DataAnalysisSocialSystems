import os

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

from plottingCasu2 import BoxplotCasu2

def ReadData(url: str) -> pd.DataFrame: 
    """    This function downloads the data from a GoogleTable sheet with the given link and transformes them into a 
    csv and then reads them in into a pd.DataFrame

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

def TestNormalDistribution(DataList):
    statistic1, p_shapiro1 = stats.shapiro(DataList[0])
    statistic2, p_ks1 = stats.kstest(DataList[0], 'norm', mode='exact')
    statistic3, p_shapiro2 = stats.shapiro(DataList[1])
    statistic4, p_ks2 = stats.kstest(DataList[1], 'norm', mode='exact')

    if p_shapiro1 >= 0.05 and p_ks1 >= 0.05 and p_shapiro2 >= 0.05 and p_ks2 >= 0.05:
        DataList.append(True)
        return DataList

    elif p_shapiro1 < 0.05 or p_ks1 < 0.05 or p_shapiro2 < 0.05 or p_ks2 < 0.05:
        DataList.append(False)
        return DataList

    elif p_ks1 >= 0.05 and p_ks2 >= 0.05:
        DataList.append(True)
        return DataList

def statisticalTestingDependent(DataList):
    if DataList[2] == True:
        statistic, p_val = stats.ttest_rel(DataList[0], DataList[1], alternative='two-sided')
        return f'The students-T-test for dependent dataset returns a p value of {p_val} with a statistic of {statistic}'
    elif DataList[2] == False:
        statistic, p_val = stats.wilcoxon(DataList[0], DataList[1], zero_method='pratt', alternative='two-sided')
        return f'The Wilcoxen-Pratt signed rank test returns a p value of {p_val} with a statistic of {statistic}'

def statisticalTestingIndependent(DataList):
    if DataList[2] == True:
        statistic, p_lev = stats.levene(DataList[0], DataList[1])
        if p_lev >= 0.05:
            statistic, p_val = stats.ttest_ind(DataList[0], DataList[1], equal_var=True, alternative='two-sided')
            return f'The students-T-test with equal variance returns a p value of {p_val} with a statistic of {statistic}'
        elif p_lev < 0.05:
            statistic, p_val = stats.ttest_ind(DataList[0], DataList[1], equal_var=False, alternative='two-sided')
            return f'The students-T-test with no equal variance returns a p value of {p_val} with a statistic of {statistic}'
    elif DataList[2] == False:
        statistic, p_val = stats.mannwhitneyu(DataList[0], DataList[1], use_continuity=True, alternative='two-sided')
        return f'The MannWhitney-U test returns a p value of {p_val} with a statistic of {statistic}'

df = ReadData('add DataURL')
df_controlTemp = ReadData('add DataURL')
df_controlNoTemp = ReadData('add DataURL')

Temp, Bees = dfProcessing(df, 6, 'Temp', 'Bienen')
Temp_cont, noTemp_cont = dfProcessing(df_controlTemp, 5, 'CasuT', 'CasunT')
noTemp1_cont, noTemp2_cont = dfProcessing(df_controlNoTemp, 5, 'Casu1', 'Casu2')

plot1 = [0, noTemp_cont, Bees]
plot2 = [0, Temp_cont, Temp]
control1 = [noTemp2_cont, 0, 0]
control2 = [noTemp1_cont, 0, 0]

TestDataDep = [
    [noTemp1_cont, noTemp2_cont],
    [Temp_cont, noTemp_cont],
    [Temp, Bees]
]

for i in TestDataDep:
    i_modified = TestNormalDistribution(i)
    result = statisticalTestingDependent(i_modified)
    print(result)

TestDataInd = [
    [noTemp_cont, Bees],
    [Temp, Temp_cont]
    ]

for i in TestDataInd:
    i_modified = TestNormalDistribution(i)
    result = statisticalTestingIndependent(i_modified)
    print(result)

labels = ['control\nN=7', 'empty vs Temp\nN=8', 'Bees vs Temp\nN=13']
path = os.path.realpath(os.path.dirname(__file__))
path = os.path.join(path, '..', 'graphs')

BoxplotCasu2(control1, control2, plot1, plot2, labels, path)
