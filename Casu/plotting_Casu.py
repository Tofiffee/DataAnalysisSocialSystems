import os

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator
import numpy as np



def plotting_plot(
    x_axis, y_casu_1, y_casu_2, mean_casu_1, mean_casu_2,
    plotBees, plotTemp, plotNoTempCont, plotTempCont
):
    path = os.path.dirname(os.path.realpath(__file__))
    
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)
    WIDTH = 0.25

    fig1 = plt.figure(figsize=(20, 15))
    ax = plt.subplot(2, 10, (1, 10))
    ax0 = plt.subplot(2, 10, (11, 16))
    ax1 = plt.subplot(2, 10, (17, 20))
    ax.set_xlim(10, 960)
    ax.set_ylim(0, 10)
    ax.xaxis.set_major_locator(MultipleLocator(60))
    ax.set_ylabel('Number of bees', fontsize=25, labelpad=10)
    ax.set_xlabel('Time [s]', fontsize=25, labelpad=10)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax0.tick_params(axis='y', which='major', labelsize=16)
    ax.text(-35, 8.5, 'A', fontdict={'fontsize': 45})
    ax0.text(-0.9, 90, 'B', fontdict={'fontsize': 45})
    
    for i in y_casu_1:
        ax.plot(x_axis, i, color='red', alpha=0.5, linewidth=0.5, linestyle=(0, (5, 5)))

    for j in y_casu_2:
        ax.plot(x_axis, j, color='blue', alpha=0.5, linewidth=0.5, linestyle=(0, (5, 5)))

    ax.plot(x_axis, mean_casu_2, color='red', linewidth=1)
    ax.plot(x_axis, mean_casu_1, color='blue', linewidth=1)

    ax.vlines(300, 0, 11, colors='k', linestyles='dashed')
    ax.vlines(320, 0, 11, colors='k', linestyles='dashed')


    ax0.set_ylim(0, 100)

    ax0.plot(x_axis, plotBees, color='blue', linewidth=1)
    ax0.plot(x_axis, plotTemp, color='red', linewidth=1)
    ax0.plot(x_axis, plotNoTempCont, color='blue', linewidth=1)
    ax0.plot(x_axis, plotTempCont, color='red', linewidth=1)


    ax0.legend(loc='upper right', fontsize=16)
    ax0.set_ylabel('Bees [%]', labelpad=10, fontsize=25)
    ax0.set_xlabel('Time [s]', labelpad=10, fontsize=25)

    # ax0.annotate('***', xy=(0, 85), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)
    # ax0.annotate('***', xy=(1, 70), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)
    # ax0.annotate('***', xy=(2, 60), xytext=(0, 0), textcoords='offset points', ha='center', va='bottom', fontsize=25)

    # x1, x2, y, h, col = 0.88, 1.86, 43, 2, 'k'
    # ax0.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=2, c=col)
    # ax0.text((x1+x2)*.5, y+h, "***", ha='center', va='bottom', color=col, fontsize=30)

    # x1, x2, y, h, col = 1.13, 2.126, 58, -2, 'k'
    # ax0.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=2, c=col)
    # ax0.text((x1+x2)*.5, y+h, "***", ha='center', va='bottom', color=col, fontsize=30)

    fig1.tight_layout()
    plt.savefig(os.path.join(path, '..', 'graphs', 'casuexp_1_line_plot.png'))


