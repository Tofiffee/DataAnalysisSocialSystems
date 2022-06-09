from plotting_Casu import plotting_plot
from DataProcessingCasu2 import labels, control1, control2, plot1, plot2
import pandas as pd

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

def CalcMean(df):
    df_erst = df[['erst_A1', 'erst_A2',	'erst_A3', 'erst_A4', 'erst_A5', 'erst_A6', 
        'erst_A7', 'erst_B1', 'erst_B2', 'erst_B3', 'erst_B4', 'erst_B5', 'erst_B6', 
        'erst_B7',	'erst_C1', 'erst_C2', 'erst_C3', 'erst_C4']]
    df_danach = df[['danach_A1', 'danach_A2',	'danach_A3', 'danach_A4', 'danach_A5',
        'danach_A6', 'danach_A7', 'danach_B1', 'danach_B2', 'danach_B3', 'danach_B4', 
        'danach_B5', 'danach_B6', 'danach_B7',	'danach_C1', 'danach_C2', 'danach_C3', 
        'danach_C4']]
    
    df_erst['mean'] = df_erst.mean(axis=1)
    df_danach['mean'] = df_danach.mean(axis=1)
  
    return df_erst['mean'], df_danach['mean']



def main():
    df = ReadData('add DataURL')
    data_list = DataPrepariation(df)
    mean_casu_1, mean_casu_2 = CalcMean(df)

    plotting_plot(
        data_list[0], data_list[1], data_list[2], mean_casu_1, mean_casu_2,
        control1, control2, plot1, plot2, labels
    )


if __name__=='__main__':
    main()


