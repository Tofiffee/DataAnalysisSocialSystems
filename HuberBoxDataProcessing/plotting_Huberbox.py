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
