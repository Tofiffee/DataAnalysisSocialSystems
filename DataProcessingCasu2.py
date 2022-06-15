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

def CalcMean(df, list1, list2, BeeNumber):
    df1 = df[list1]
    df2 = df[list2]
    
    df1['mean'] = df1.mean(axis=1)
    df2['mean'] = df1.mean(axis=1)
    df1['mean'] = df1['mean']/BeeNumber * 100
    df2['mean'] = df2['mean']/BeeNumber * 100
  
    return df1['mean'], df2['mean']

# def dfProcessing(df, beeNumber, keyword1, keyword2):
#     array1 = np.array([])
#     array2 = np.array([])

#     for column in df.columns.values.tolist()[1:]:
#         df[f'{column}'] = df[f'{column}'].apply(lambda x: x/beeNumber*100)
#         if keyword1 in column:
#             array = df[f'{column}'].to_numpy()
#             array1 = np.hstack((array1, array))
#         elif keyword2 in column:
#             array = df[f'{column}'].to_numpy()
#             array2 = np.hstack((array2, array))

#     return array1, array2

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

df = ReadData('https://docs.google.com/spreadsheets/d/1c5eXRyP4uLSDKJ_1PHlx48nZ8wQ06mUr1Ayrty-kfDg/edit#gid=0')
df_controlTemp = ReadData('https://docs.google.com/spreadsheets/d/1rtl7NfzKXGVWi90JLlAunum5BX6TK17NUiaficQs9q0/edit#gid=0')

plotBees, plotTemp = CalcMean(
    df,
    ['Bienen_A1', 'Bienen_A2', 'Bienen_B1', 'Bienen_B2', 'Bienen_D1', 'Bienen_D2', 'Bienen_D3','Bienen_D4', 'Bienen_E1', 'Bienen_F1', 'Bienen_F2', 'Bienen_F3', 'Bienen_F4'],
    ['Temp_A1', 'Temp_A2', 'Temp_B1', 'Temp_B2', 'Temp_D1', 'Temp_D2', 'Temp_D3', 'Temp_D4', 'Temp_E1', 'Temp_F1', 'Temp_F2', 'Temp_F3', 'Temp_F4'],
    6
)
plotNoTempCont, plotTempCont = CalcMean(
    df_controlTemp,
    ['CasunT_A', 'CasunT_B', 'CasunT_C', 'CasunT_D', 'CasunT_E', 'CasunT_F', 'CasunT_G', 'CasunT_H'],
    ['CasuT_Alinks','CasuT_B_unten', 'CasuT_C_links', 'CasuT_D_unten', 'CasuT_E_rechts', 'CasuT_F_unten', 'CasuT_G_unten', 'CasuT_H_unten'],
    5
)



# TestDataDep = [
#     [Temp_cont, noTemp_cont],
#     [Temp, Bees]
# ]

# for i in TestDataDep:
#     i_modified = TestNormalDistribution(i)
#     result = statisticalTestingDependent(i_modified)
#     print(result)

# TestDataInd = [
#     [noTemp_cont, Bees],
#     [Temp, Temp_cont]
#     ]

# for i in TestDataInd:
#     i_modified = TestNormalDistribution(i)
#     result = statisticalTestingIndependent(i_modified)
#     print(result)

# labels = ['control\nN=7', 'empty vs Temp\nN=8', 'Bees vs Temp\nN=13']
# path = os.path.realpath(os.path.dirname(__file__))
# path = os.path.join(path, '..', 'graphs')