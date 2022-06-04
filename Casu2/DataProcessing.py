import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def ReadData(url: str) -> pd.DataFrame: 
    """    This function downloads the data from a GoogleTable sheet with the given link and transformes them into a csv and then reads them in into a pd.DataFrame

    Args:
        url (str): 

    Returns:
        pd.DataFrame: _description_
    """
    url_read = url.replace('/edit#gid=', '/export?format=csv&gid=')

    df = pd.read_csv(url_read, on_bad_lines='skip')

    return df

df = ReadData('https://docs.google.com/spreadsheets/d/1c5eXRyP4uLSDKJ_1PHlx48nZ8wQ06mUr1Ayrty-kfDg/edit#gid=0')

TempArray = np.array([])
BeesArray = np.array([])

for column in df.columns.values.tolist()[1:]:
    df[f'{column}'] = df[f'{column}'].apply(lambda x: x/6*100)
    if 'Temp' in column:
        array = df[f'{column}'].to_numpy()
        TempArray = np.hstack((TempArray, array))
    elif 'Biene' in column:
        array = df[f'{column}'].to_numpy()
        BeesArray = np.hstack((BeesArray, array))

statistic1, p_shapiro1 = stats.shapiro(TempArray)
statistic2, p_ks1 = stats.kstest(TempArray, 'norm', mode='exact')
statistic3, p_shapiro2 = stats.shapiro(BeesArray)
statistic4, p_ks2 = stats.kstest(BeesArray, 'norm', mode='exact')

print(p_shapiro1, p_ks1)
print(p_shapiro2, p_ks2)

labels = ['Bees vs Temp']
x_axis = np.arange(len(labels))
WIDTH = 0.25

fig0, ax0 = plt.subplots(figsize=(12, 10))
ax0.set_ylim(0, 100)


plota1 = ax0.boxplot(TempArray, positions=x_axis - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
            boxprops=dict(facecolor='lightsteelblue', color='k'),
            capprops=dict(color='k'),
            whiskerprops=dict(color='k'),
            flierprops=dict(color='k', markeredgecolor='k'),
            medianprops=dict(color='k'))

plota2 = ax0.boxplot(BeesArray, positions=x_axis + WIDTH/2 + 0.01, widths=WIDTH, notch=False, patch_artist=True,
            boxprops=dict(facecolor='lightcoral', color='k'),
            capprops=dict(color='k'),
            whiskerprops=dict(color='k'),
            flierprops=dict(color='k', markeredgecolor='k'),
            medianprops=dict(color='k'))

ax0.grid(which='major', axis='y', linewidth=1, linestyle=(0, (1, 10)), color='black')
ax0.set_xticks(ticks=x_axis, labels=labels, fontsize=16)

fig0.tight_layout()
plt.savefig('Boxplot_Casu2.png')
