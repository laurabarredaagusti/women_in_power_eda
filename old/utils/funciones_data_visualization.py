
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib as mpl


enmax_palette = ["#c5c5c5", "#f54939", "#2018c2", '#a1a1a1', '#838383']
color_codes_wanted = ['grey1', 'red', 'blue', 'grey2', 'grey3']
c = lambda x: enmax_palette[color_codes_wanted.index(x)]
# csfont = {'fontname':'PP Neue Montreal'}
mpl.rcParams['font.size'] = 15
mpl.rcParams['font.sans-serif'] = 'PP Neue Montreal'

def pie_plot_general(data1, data2, labels_pie, title):
    '''
    Funcion que crea un pieplot único
    '''
    csfont = {'fontname':'PP Neue Montreal'}
    fig, ax = plt.subplots(facecolor=c("grey1"))
    ax.set_facecolor(c("grey1"))
    data = [data1, data2]
    colors = [c('red'), c('grey2')]
    pie_plot = plt.pie(data, labels = None, colors = colors, autopct='%.0f%%')
    plt.legend(labels=labels_pie,loc = 2, bbox_to_anchor = (1,1), prop={'size': 15}, facecolor=c('grey1'), edgecolor='white')
    plt.title(title, pad=30, fontsize = 15, **csfont)
    return pie_plot

def bar_doble(df, labels, title):
    '''
    Funcion que devuelve un gráfico de barras dobles
    '''
    bar_plot = df.plot(kind='bar')
    plt.legend(labels=labels, fontsize = 'small',loc = 2, bbox_to_anchor = (1,1), prop={'size': 12})
    plt.title(title, pad=30)
    plt.grid(color='white', linestyle='-.', linewidth=.2)
    return bar_plot


def pie_plot_inside_grid4(data1, data2,ax1, ax2):
    '''
    Función que crea un pie plot preparado para estar dentro de un grid de 4x4
    '''
    csfont = {'fontname':'PP Neue Montreal'}

    data = [data1, data2]
    colors = [c('red'), c('grey2')]
    pie_plot_total = axs[ax1, ax2].pie(data, colors = colors, autopct='%.0f%%')
    return pie_plot_total


def line_plot_comparison_years(dataframe, valor_x, valor_y, valor_hue, ax_number, title):
    colors = [c('red'), c('grey2')]
    sns.set(rc={'axes.facecolor':c('grey1')})
    sns.set_palette(sns.color_palette(colors))
    line_plot_comparison = sns.lineplot(data=dataframe, x=valor_x, y=valor_y, hue=valor_hue, ax=ax_number).set(title=title)
    return line_plot_comparison