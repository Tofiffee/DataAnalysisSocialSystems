import os

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator
import numpy as np



def plotting_plot(
    x_axis, y_casu_1, y_casu_2, mean_casu_1, mean_casu_2,
    control1, control2, array1, array2, labels
):
    path = os.path.dirname(os.path.realpath(__file__))
    
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)
    WIDTH = 0.25

    fig1 = plt.figure(figsize=(20, 15))
    ax = plt.subplot(2, 3, (1, 3))
    ax0 = plt.subplot(2, 3, (4, 5))
    ax.set_xlim(10, 960)
    ax.set_ylim(0, 10)
    ax.xaxis.set_major_locator(MultipleLocator(60))
    ax.set_ylabel('Number of bees', fontsize=20, labelpad=10)
    ax.set_xlabel('Time [s]', fontsize=20, labelpad=10)

    for i in y_casu_1:
        ax.plot(x_axis, i, color='red', alpha=0.5, linewidth=0.5, linestyle=(0, (5, 5)))

    for j in y_casu_2:
        ax.plot(x_axis, j, color='blue', alpha=0.5, linewidth=0.5, linestyle=(0, (5, 5)))

    ax.plot(x_axis, mean_casu_1, color='red', linewidth=1)
    ax.plot(x_axis, mean_casu_2, color='blue', linewidth=1)

    ax.vlines(300, 0, 11, colors='k', linestyles='dashed')
    ax.vlines(320, 0, 11, colors='k', linestyles='dashed')

    x_axis_boxplot = np.arange(len(labels))
    ax0.set_ylim(0, 100)

    plota1 = ax0.boxplot(array1, positions=x_axis_boxplot - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightsteelblue', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='red'))

    plota2 = ax0.boxplot(array2, positions=x_axis_boxplot + WIDTH/2 + 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightcoral', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='red'))

    plotb1 = ax0.boxplot(control1, positions=x_axis_boxplot - WIDTH/2 - 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='dimgray', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='red'))

    plotb2 = ax0.boxplot(control2, positions=x_axis_boxplot + WIDTH/2 + 0.01, widths=WIDTH, notch=False, patch_artist=True,
                boxprops=dict(facecolor='lightgray', color='k'),
                capprops=dict(color='k'),
                whiskerprops=dict(color='k'),
                flierprops=dict(color='k', markeredgecolor='k'),
                medianprops=dict(color='red'))


    ax0.grid(which='major', axis='y', linewidth=1, linestyle=(0, (1, 10)), color='black')
    ax0.set_xticks(ticks=x_axis_boxplot, labels=labels, fontsize=16)
    ax0.legend([plotb1['boxes'][0], plotb2['boxes'][0], plota1['boxes'][0], plota2['boxes'][0]], ['left/upper', 'right/lower' , '26 degree', '36 degree'], bbox_to_anchor=(1.2, 1.01), 
    loc='upper right', fontsize=16)
    ax0.set_ylabel('Bees [%]', labelpad=10, fontsize=25)
    ax0.set_xlabel('Experiments', labelpad=10, fontsize=25)

    ax0.annotate('***', xy=(0, 85), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)
    ax0.annotate('***', xy=(1, 70), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)
    ax0.annotate('***', xy=(2, 60), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)

    x1, x2, y, h, col = 0.88, 1.86, 43, 2, 'k'
    ax0.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=2, c=col)
    ax0.text((x1+x2)*.5, y+h, "***", ha='center', va='bottom', color=col, fontsize=30)

    x1, x2, y, h, col = 1.13, 2.126, 58, -2, 'k'
    ax0.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=2, c=col)
    ax0.text((x1+x2)*.5, y+h, "***", ha='center', va='bottom', color=col, fontsize=30)

    fig1.tight_layout()
    plt.savefig(os.path.join(path, '..', 'graphs', 'casuexp_1_line_plot.png'))


