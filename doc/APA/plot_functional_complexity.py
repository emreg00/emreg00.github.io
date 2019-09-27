
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def plot_functional_complexity(x):
    # Use numpy for function value calculation
    x = np.array(x)
    y_log = np.log(x)
    y_sqrt = np.sqrt(x)
    y_log = np.log(x)
    y_n = x
    y_n2 = x*x
    y_exp = np.power(2,x)

    # Plot 
    fig, ax = plt.subplots()
    ax.plot(x, y_log, 'C1', label='logarithmic') # plt.plot(x, y_log, 'C1') 
    ax.plot(x, y_sqrt, 'C2', label='square-root')
    ax.plot(x, y_n, 'C3', label='linear')
    ax.plot(x, y_n2, 'C4', label='quadratic')
    ax.plot(x, y_exp, 'C5', label='exponential')

    # Legend and axes
    ax.legend(loc='upper right', shadow=True, title='Function') # fontsize='x-large', 
    #plt.legend(title='Function')
    ax.set(xlabel='N (Input size)', ylabel='Complexity (# of operations)', title='Functional complexity')
    ax.set_xlim([0,100])
    ax.set_ylim([0,1000])
    ax.grid()

    fig.savefig("output_plot.png")
    plt.show()
    return plt


if __name__ == "__main__":
    x = [1,10,50,100]
    plot_functional_complexity(x)


