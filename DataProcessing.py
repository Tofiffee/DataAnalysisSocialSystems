from plotting import plotting_plot

import pandas as pd
import matplotlib.pyplot as plt

def ReadData(): 
    """
    This function downloads the data from a GoogleTable sheet with the given link and transformes them into a a csv file
    """
    url = 'https://docs.google.com/spreadsheets/d/11DkhIY7QQkUMNtjX1b16j7DmmQ6woKyCrGO_3p-Avig/edit#gid=0'
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

def CalcMean(df):
    df_erst = df[['erst_A1', 'erst_A2',	'erst_A3', 'erst_A4', 'erst_A5', 'erst_A6', 'erst_A7', 'erst_B1', 'erst_B2', 'erst_B3', 'erst_B4', 'erst_B5', 'erst_B6', 'erst_B7',	'erst_C1', 'erst_C2', 'erst_C3', 'erst_C4']]
    df_danach = df[['danach_A1', 'danach_A2',	'danach_A3', 'danach_A4', 'danach_A5', 'danach_A6', 'danach_A7', 'danach_B1', 'danach_B2', 'danach_B3', 'danach_B4', 'danach_B5', 'danach_B6', 'danach_B7',	'danach_C1', 'danach_C2', 'danach_C3', 'danach_C4']]

    return df_erst, df_danach



def main():
    df = ReadData()
    data_list = DataPrepariation(df)
    plotting_plot(data_list[0], data_list[1], data_list[2])
    df1, df2 = CalcMean(df)
    df1['mean'] = df1.mean(axis=1)
    df2['mean'] = df2.mean(axis=1)
    print(df1.head(10))
    print(df2.head(10))



if __name__=='__main__':
    main()


