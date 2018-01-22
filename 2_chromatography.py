#! -*- coding: utf-8 -*-

import pandas
import matplotlib.pyplot as plt


def process(filename, title):
    data = pandas.read_csv('res_down.csv')

    data['t'] = pandas.Series([(t - data['t'][i - 1] if i != 0 else t) for i, t in enumerate(data['t'])])
    data['x_norm'] = data['x'] * 0.001

    data['v'] = pandas.Series([0.005 / t for t in data['t']])
    data['delta_v'] = pandas.Series([(0.1 + (0.3 / t)) * (0.005 / t) for t in data['t']])

    data['x2_norm'] = data['x_norm'] ** 2
    data['delta_x2'] = pandas.Series([(x ** 2) * (0.001 / x) for x in data['x_norm']])

    data['1/x_norm'] = 1 / data['x_norm']
    data['delta_1/x'] = pandas.Series([(1 / x) * (0.001 / x) for x in data['x_norm']])

    print(data)

    plt.title(title)
    plt.ylabel(u'$x^2,\, м^2$')
    plt.xlabel('$t$')
    for row in data.as_matrix():
        plt.errorbar(x=row[1], y=row[5],
                     xerr=0.3, yerr=row[6],
                     label=True, color='#C00000')

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()

    plt.title(title)
    plt.xlabel(u'$1/x,\, м^{-1}$')
    plt.ylabel(u'$V, м/с$')
    for row in data.as_matrix():
        plt.errorbar(x=row[7], y=row[3],
                     xerr=row[8], yerr=row[4],
                     label=True, color='#0000C0')

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()


process('data_down.csv', u'Вниз по капилляру')
process('data_up.csv', u'Вверх по капилляру')
