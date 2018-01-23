#! -*- coding: utf-8 -*-

import pandas
import matplotlib.pyplot as plt


def process(filename, title):
    data = pandas.read_csv(filename)

    data['t_dif'] = pandas.Series([(t - data['t'][i - 1] if i != 0 else t) for i, t in enumerate(data['t'])])
    data['x_norm'] = data['x'] * 0.001
    data['dist'] = pandas.Series([(x - data['x_norm'][i - 1] if i != 0 else x) for i, x in enumerate(data['x_norm'])])
    data['int_center'] = pandas.Series([x - data['dist'][i] / 2 for i, x in enumerate(data['x_norm'])])

    data['v'] = pandas.Series([data['dist'][i] / t for i, t in enumerate(data['t_dif'])])
    data['delta_v'] = pandas.Series([((0.001 / data['dist'][i]) + (0.3 / t)) * data['v'][i]
                                     for i, t in enumerate(data['t_dif'])])

    data['x2_norm'] = data['int_center'] ** 2
    data['delta_x2'] = pandas.Series([data['x2_norm'][i] * (0.001 / x) for i, x in enumerate(data['int_center'])])

    data['1/x_norm'] = 1 / data['int_center']
    data['delta_1/x'] = pandas.Series([(1 / x) * (0.001 / x) for x in data['int_center']])

    print(data)

    plt.title(title)
    plt.ylabel(u'$x^2,\, м^2$')
    plt.xlabel('$t$')
    for row in data.as_matrix():
        plt.errorbar(x=row[1], y=row[8],
                     xerr=0.3, yerr=row[9],
                     label=True, color='#C00000')

    mng = plt.get_current_fig_manager()
    try:
        mng.window.state('zoomed')

    except Exception:
        try:
            mng.resize(*mng.window.maxsize())
        except Exception:
            pass

    plt.show()

    plt.title(title)
    plt.xlabel(u'$1/x,\, м^{-1}$')
    plt.ylabel(u'$V, м/с$')
    for row in data.as_matrix():
        plt.errorbar(x=row[10], y=row[6],
                     xerr=row[11], yerr=row[7],
                     label=True, color='#0000C0')

    mng = plt.get_current_fig_manager()
    try:
        mng.window.state('zoomed')

    except Exception:
        try:
            mng.resize(*mng.window.maxsize())
        except Exception:
            pass

    plt.show()


process('res_down.csv', u'Вниз по капилляру')
process('res_up.csv', u'Вверх по капилляру')
