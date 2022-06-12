from plotting_Casu import plotting_plot
import os
from Statistics import StatisticalTesting

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

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

def DataPrepariation(df):
    casu = df.columns.values.tolist()
    casu_1 = [x for x in casu if 'erst' in x]
    casu_2 = [x for x in casu if 'danach' in x]


    x_axis = df[f'{casu[0]}']
    y_casu_1 = []
    y_casu_2 = []
    
    for i in casu_1:
        y_casu_1.append(df[f'{i}'])

    for j in casu_2:
        y_casu_2.append(df[f'{j}'])

    return [x_axis, y_casu_1, y_casu_2]

def CalcMean(df, list1, list2, BeeNumber):
    df1 = df[list1]
    df2 = df[list2]
    
    df1['mean'] = df1.mean(axis=1)
    df2['mean'] = df2.mean(axis=1)
    df1['mean'] = df1['mean'].apply(lambda x: x/BeeNumber * 100 if x != 0 else x)
    df2['mean'] = df2['mean'].apply(lambda x: x/BeeNumber * 100 if x != 0 else x)
  
    return df1, df2

def main():
    df = ReadData('https://docs.google.com/spreadsheets/d/11DkhIY7QQkUMNtjX1b16j7DmmQ6woKyCrGO_3p-Avig/edit#gid=0')
    df_Temp = ReadData('https://docs.google.com/spreadsheets/d/1c5eXRyP4uLSDKJ_1PHlx48nZ8wQ06mUr1Ayrty-kfDg/edit#gid=0')
    df_controlTemp = ReadData('https://docs.google.com/spreadsheets/d/1rtl7NfzKXGVWi90JLlAunum5BX6TK17NUiaficQs9q0/edit#gid=0')
    
    data_list = DataPrepariation(df)
    mean_casu1, mean_casu2 = CalcMean(
    df,
    ['erst_A1', 'erst_A2',	'erst_A3', 'erst_A4', 'erst_A5', 'erst_A6', 'erst_A7', 'erst_B1', 'erst_B2', 'erst_B3', 'erst_B4', 'erst_B5', 'erst_B6', 'erst_B7',	'erst_C1', 'erst_C2', 'erst_C3', 'erst_C4'],
    ['danach_A1', 'danach_A2',	'danach_A3', 'danach_A4', 'danach_A5', 'danach_A6', 'danach_A7', 'danach_B1', 'danach_B2', 'danach_B3', 'danach_B4', 'danach_B5', 'danach_B6', 'danach_B7',	'danach_C1', 'danach_C2', 'danach_C3', 'danach_C4'],
    100
    )
    plotBees, plotTemp = CalcMean(
        df_Temp,
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

    print(plotBees.iloc[-1]['mean'])

    plotting_plot(
        data_list[0], data_list[1], data_list[2], mean_casu1['mean'], mean_casu2['mean'],
        plotBees['mean'], plotTemp['mean'], plotNoTempCont['mean'], plotTempCont['mean'],
        [plotNoTempCont.iloc[-1]['mean'], plotBees.iloc[-1]['mean']],
        [plotTempCont.iloc[-1]['mean'], plotTemp.iloc[-1]['mean']],
        ['noTemp vs Temp', 'Bees vs Temp']
        )

    print(plotBees.iloc[-1].tolist()[:-1])
    
    testData = [
        {'Data1': plotBees.iloc[-1].tolist()[:-1], 'Data2': plotTemp.iloc[-1].tolist()[:-1], 
        'dependent': True, 'alternativ': 'less'},
        {'Data1': plotNoTempCont.iloc[-1].tolist()[:-1], 'Data2': plotTempCont.iloc[-1].tolist()[:-1], 
        'dependent': True, 'alternativ': 'less'},
        {'Data1': plotNoTempCont.iloc[-1].tolist()[:-1], 'Data2': plotBees.iloc[-1].tolist()[:-1], 
        'dependent': False, 'alternativ': 'less'}
        ]

    for i in testData:
        result = StatisticalTesting(i)
        print(result)

if __name__=='__main__':
    main()
