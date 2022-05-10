import matplotlib.pyplot as plt
import seaborn as sns
import os


def plotting_plot(x_axis, y_casu_1, y_casu_2):
    path = os.path.dirname(os.path.realpath(__file__))
    
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)

    fig1, ax = plt.subplots(figsize=(20, 10))

    for i in y_casu_1:
        plt.plot(x_axis, i, color='red')

    for j in y_casu_2:
        plt.plot(x_axis, j, color='blue')

    plt.savefig('casuexp_1_line_plot.png')


