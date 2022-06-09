import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import os

def boxplot(
    listA1: iter, listA2: iter, x_axis_A: iter, label_A: iter,
    listB1: iter, listB2: iter, x_axis_B: iter, label_B: iter
    ) -> plt.figure:
    """creates a figure (boxplot) for the given data for the speed and the socail time for one, two and three bees+

    Args:
        listA1 (iter): social time for two and three bees at 26 degrees
        listA2 (iter): social time for two and three bees at 36 degrees
        x_axis_A (iter): np.arange(len(listA1)), gives the amount of x-ticks that are needed for the plot
        label_A (iter): lables that should be ploted on the x-axis of the upper boxplot
        listB1 (iter): speeds for one, two and three bees at 26 degrees
        listB2 (iter): speeds for one, two and three bees at 36 degrees
        x_axis_B (iter): np.arange(len(list(B1)), gives the amount of x-ticks that are needed for the plot
        label_B (iter): lables that should be ploted on the x-axis of the lower boxplot

    Returns:
        plt.figure: save a figure with the two boxplots in the folder graphs
    """
    # seaborn standard config Toffifee
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)

    path = os.path.dirname(os.path.realpath(__file__))
    WIDTH = 0.25

    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)

    fig0, (ax0, ax1) = plt.subplots(2, 1, figsize=(12, 10))
    AXIS = (ax0, ax1)
    ax0.set_ylim(0, 25)
    ax1.set_ylim(0, 7)
    
    # all settings that are needed for both plots
    for ax in AXIS:
        ax.grid(which='major', axis='y', linewidth=1, linestyle=(0, (1, 10)), color='black')

    # plot of the social time for two and three bees at 26 degrees
    plota1 = ax0.boxplot(listA1, positions=x_axis_A - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightsteelblue', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    # plot of the social time for two and three bees at 36 degrees
    plota2 = ax0.boxplot(listA2, positions=x_axis_A + WIDTH/2 + 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightcoral', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    # plot of the speeds for one, two and three bees at 26 degrees
    plotb1 = ax1.boxplot(listB1, positions=x_axis_B - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightsteelblue', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='k'))

    # plot of the speeds for one, two and three bees at 26 degrees
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
    ax0.text(-0.85, 21, 'A', fontdict={'fontsize': 45})
    ax1.text(-0.9, 6.1, 'B', fontdict={'fontsize': 45})
    ax0.tick_params(axis='y', which='major', labelsize=16)
    ax1.tick_params(axis='y', which='major', labelsize=16)
    
    ax0.text(-0.19, 11, 'N=11', fontdict={'fontsize': 16})
    ax0.text(0.08, 22, 'N=11', fontdict={'fontsize': 16})
    ax0.text(0.82, 6, 'N=6', fontdict={'fontsize': 16})
    ax0.text(1.09, 5, 'N=6', fontdict={'fontsize': 16})

    ax1.text(-0.3, 2.4, 'N=6', fontdict={'fontsize': 16})
    ax1.text(0.18, 3, 'N=5', fontdict={'fontsize': 16})
    
    ax1.text(0.65, 2.3, 'N=22', fontdict={'fontsize': 16})
    ax1.text(1.18, 2.8, 'N=22', fontdict={'fontsize': 16})
    
    ax1.text(1.7, 2.1, 'N=6', fontdict={'fontsize': 16})
    ax1.text(2.18, 2.4, 'N=6', fontdict={'fontsize': 16})




    fig0.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(path), 'graphs', 'Boxplot_TimeTogether.png'))