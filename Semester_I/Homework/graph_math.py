import numpy as np
import matplotlib.pyplot as plt

np.seterr(divide='ignore', invalid='ignore')

def graph(functions=[], min_value=-5.0, max_value=5.0, value=10, name='',
          inter=None, asin=None, display=5, x_label=0,spaces=0):
    x = np.linspace(min_value, max_value, value)

    fig, ax1= plt.subplots(figsize=(12, 6))

    for function, name, color in zip(functions, name, ['black', 'r', 'g', 'b']):
      ax1.plot(x, function(x), color, label=name)

    ax1.spines['left'].set_position('zero')
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')

    ax1.set_xlabel("x")
    ax1.set_ylabel("y")

    ax1.yaxis.set_label_coords(0, 0.5)
    ax1.xaxis.set_label_coords(1, 0.4+x_label)
    if inter:
        for point in inter:
            x_inter, y_inter = point
            ax1.plot(x_inter, y_inter, 'ro',
                     label=f'Punto de intersección: ({x_inter:.2f}, {y_inter:.2f})',
                     zorder=3)
    if asin:
        ax1.axhline(y=asin, color='black', linestyle='--',
                    label='Asíntota horizontal', zorder=2)
    ax1.legend(loc='upper left')

    plt.tight_layout()
    plt.show()
    print('\n'*spaces)


