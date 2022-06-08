import os

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def BoxplotCasu2(array1, array2, labels, path):
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)
    
    WIDTH = 0.25
    x_axis = np.arange(len(labels))

    fig0, ax0 = plt.subplots(figsize=(12, 10))
    ax0.set_ylim(0, 100)


    plota1 = ax0.boxplot(array1, positions=x_axis - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightsteelblue', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    plota2 = ax0.boxplot(array2, positions=x_axis + WIDTH/2 + 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightcoral', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))


    ax0.grid(which='major', axis='y', linewidth=1, linestyle=(0, (1, 10)), color='black')
    ax0.set_xticks(ticks=x_axis, labels=labels, fontsize=16)
    ax0.legend(loc='best')

    fig0.tight_layout()
    plt.savefig(os.path.join(path, 'Boxplot_Casu2.png'))