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

def boxplot(listA1, listA2, x_axis_A, label_A, listB1, listB2, x_axis_B, label_B):
    path = os.path.dirname(os.path.realpath(__file__))
    WIDTH = 0.25

    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)

    fig0, (ax0, ax1) = plt.subplots(2, 1, figsize=(12, 10))
    AXIS = (ax0, ax1)
    ax0.set_ylim(0, 25)
    ax1.set_ylim(0, 9)
    
    for ax in AXIS:
        ax.grid(which='major', axis='y', linewidth=1, linestyle=(0, (1, 10)), color='black')

    plota1 = ax0.boxplot(listA1, positions=x_axis_A - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightsteelblue', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    plota2 = ax0.boxplot(listA2, positions=x_axis_A + WIDTH/2 + 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightcoral', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    plotb1 = ax1.boxplot(listB1, positions=x_axis_B - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightsteelblue', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    plotb2 = ax1.boxplot(listB2, positions=x_axis_B + WIDTH/2 + 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightcoral', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))


    ax0.set_xticks(ticks=x_axis_A, labels=label_A, fontsize=16)
    ax1.set_xticks(ticks=x_axis_B, labels=label_B, fontsize=16)
    ax0.legend([plota1["boxes"][0], plota2["boxes"][0]], ['26 Degrees', '36 Degrees'], bbox_to_anchor=(1.005, 1), loc='upper left', fontsize=16)
    ax1.legend([plotb1["boxes"][0], plotb2["boxes"][0]], ['26 Degrees', '36 Degrees'], bbox_to_anchor=(1.005, 1.01), loc='upper left', fontsize=16)
    ax0.set_ylabel('Social Contact duration [s]', fontsize=16)
    ax1.set_ylabel('Walking speed [cm/s]', fontsize=16)
    ax0.annotate('*', xy=(0, 15), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)
    ax1.annotate('***', xy=(0, 5.5), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)
    ax1.annotate('***', xy=(1, 5.5), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)
    ax1.annotate('***', xy=(2, 5.5), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)

    fig0.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(path), 'graphs', 'Boxplot_TimeTogether.png'))