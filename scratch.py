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


def main():
    df = ReadData()

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

    print(y_casu_1)

    plotting_plot(x_axis, y_casu_1, y_casu_2)
    
    print(x_axis)

if __name__=='__main__':
    main()


