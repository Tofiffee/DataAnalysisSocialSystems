import os

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator
import numpy as np



def plotting_plot(
    x_axis, y_casu_1, y_casu_2, mean_casu_1, mean_casu_2,
    plotBees, plotTemp, plotNoTempCont, plotTempCont,
    bar1, bar2, labels,
    ):
    path = os.path.dirname(os.path.realpath(__file__))
    
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)
    WIDTH = 0.25

    fig1 = plt.figure(figsize=(20, 15))
    ax0 = plt.subplot(2, 11, (1, 11))
    ax0.set_xlim(10, 960)
    ax0.set_ylim(0, 10)
    ax0.xaxis.set_major_locator(MultipleLocator(60))
    ax0.set_ylabel('Number of bees', fontsize=25, labelpad=10)
    ax0.set_xlabel('Time [s]', fontsize=25, labelpad=10)
    ax0.tick_params(axis='both', which='major', labelsize=16)
    ax0.text(-35, 8.7, 'A', fontdict={'fontsize': 45})
    
    
    for i in y_casu_1:
        ax0.plot(x_axis, i, color='red', alpha=0.5, linewidth=0.5, linestyle=(0, (5, 5)))

    for j in y_casu_2:
        ax0.plot(x_axis, j, color='blue', alpha=0.5, linewidth=0.5, linestyle=(0, (5, 5)))

    ax0.plot(x_axis, mean_casu_1, color='red', linewidth=1, label='CASU 1')
    ax0.plot(x_axis, mean_casu_2, color='blue', linewidth=1, label='CASU 2')

    ax0.vlines(300, 0, 11, colors='k', linestyles='dashed')
    ax0.vlines(320, 0, 11, colors='k', linestyles='dashed')
    ax0.legend(loc='center right', fontsize=16)

    ax1 = plt.subplot(2, 11, (12, 16))
    ax1.set_ylim(0, 100)

    ax1.plot(x_axis, plotBees, color='blue', linewidth=1.5)
    ax1.plot(x_axis, plotTemp, color='red', linewidth=1.5)
    ax1.plot(x_axis, plotNoTempCont, color='lightsteelblue', linewidth=1.5)
    ax1.plot(x_axis, plotTempCont, color='lightcoral', linewidth=1.5)

    ax1.set_ylabel('Bees [%]', labelpad=10, fontsize=25)
    ax1.set_xlabel('Time [s]', labelpad=10, fontsize=25)
    ax1.tick_params(axis='y', which='major', labelsize=16)
    ax1.text(-0.9, 90, 'B', fontdict={'fontsize': 45})

    x_bar = np.arange(len(labels))
    WIDTH = 0.25
    
    ax2 = plt.subplot(2, 11, (17, 21))
    ax2.set_ylim(0, 100)

    ax2.bar(x_bar - WIDTH/2, [bar1[0], 0], WIDTH, color='lightsteelblue', label='26 °C no s-bees')
    ax2.bar(x_bar + WIDTH/2, [bar2[0], 0], WIDTH, color='lightcoral', label='36 °C no s-bees')
    ax2.bar(x_bar - WIDTH/2, [0, bar1[1]], WIDTH, color='blue', label='26 °C with s-bees')
    ax2.bar(x_bar + WIDTH/2, [0, bar2[1]], WIDTH, color='red', label='36 °C no s-bees')

    ax2.set_xticks(ticks=x_bar, labels=labels, fontsize=20)

    x1, x2, y, h, col = -0.125, 0.125, 98, 2, 'k'
    ax2.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=2, c=col)
    ax2.text((x1+x2)*.5, y+h, "**", ha='center', va='bottom', color=col, fontsize=30)

    x1, x2, y, h, col = 0.875, 1.125, 84, 2, 'k'
    ax2.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=2, c=col)
    ax2.text((x1+x2)*.5, y+h, "***", ha='center', va='bottom', color=col, fontsize=30)

    ax2.text(-0.27, 90, 'C', fontdict={'fontsize': 45})
    ax2.text(-0.1875, 3, 'n=8', fontdict={'fontsize': 16})
    ax2.text(0.15, 98, 'n=8', fontdict={'fontsize': 16})
    ax2.text(0.8125, 17, 'n=13', fontdict={'fontsize': 16})
    ax2.text(1.15, 84, 'n=13', fontdict={'fontsize': 16})
    ax2.set_ylabel('Bees [%]', labelpad=10, fontsize=25)
    ax2.set_xlabel('Experimental Setups' , labelpad=10, fontsize=25)

    ax2.legend(loc='upper right', fontsize=16, bbox_to_anchor=(1.2, 1.2))

    fig1.tight_layout()
    plt.savefig(os.path.join(path, '..', 'graphs', 'casuexp_1_line_plot.png'))


