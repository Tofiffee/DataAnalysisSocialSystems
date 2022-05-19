import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import os

def plot_speed_single(x_axis, data, filename):
    path = os.path.dirname(os.path.realpath(__file__))

    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)

    fig1, ax = plt.subplots(figsize=(20, 10))
    ax.set_ylim(0, np.ceil(data[0]['distancePerSec'].max()))
    ax.set_xlim(60, 660)
    
    for i in range(len(data)):    
        plt.plot(x_axis, data[i]['distancePerSec'], color='k', linewidth=1)
        
    plt.savefig(os.path.join(path, 'graphs', filename))

def boxplotTime(list1, list2, x_axis, label):
    path = os.path.dirname(os.path.realpath(__file__))
    WIDTH = 0.25

    fig0, ax0 = plt.subplots(figsize=(12, 10))
    ax0.set_ylim(0, 22)
    ax0.grid(which='major', axis='y', linewidth=1, linestyle=(0, (1, 10)), color='black')

    plotd1 = plt.boxplot(list1, positions=x_axis - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='blue', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    plotd2 = plt.boxplot(list2, positions=x_axis + WIDTH/2 + 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='red', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    plt.xticks(ticks=x_axis, labels=label, fontsize=14)
    plt.legend([plotd1["boxes"][0], plotd2["boxes"][0]], ['26 Degrees', '36 Degrees'], bbox_to_anchor=(1.005, 1), loc='upper left', fontsize=12)


    plt.savefig(os.path.join(os.path.dirname(path), 'graphs', 'Boxplot_TimeTogether.png'))