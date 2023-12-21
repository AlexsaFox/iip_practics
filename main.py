from matplotlib import pyplot as plt

from modelstorage import ModelStorage
from output import (output_ranges_of_vars, output_zero_count_of_vars, output_counts_of_model_by_algo, output_data_size,
                    output_count_vars, output_types_of_vars, draw_histogram, draw_scatter, draw_boxplot)


def main():
    ms = ModelStorage()
    ms.load_from_file()
    print('task 1')
    output_data_size(ms)
    output_count_vars(ms)
    print('Типы переменных')
    output_types_of_vars(ms)
    print('Минимум и максимум переменных')
    output_ranges_of_vars(ms)
    print('Количество отсуствующих значений в переменных')
    output_zero_count_of_vars(ms)
    print('task 6')
    output_counts_of_model_by_algo(ms)

    print('test')
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig, (ax3, ax4) = plt.subplots(1, 2)
    fig, (ax5, ax6) = plt.subplots(1, 2)

    # Histograms
    draw_histogram(ms,'time', ax1)
    draw_histogram(ms,'iterations', ax2)

    # Scatters
    draw_scatter(ms,'goal_fit', 'params', ax3)
    draw_scatter(ms,'params', 'iterations', ax4)

    draw_scatter(ms, 'goal_fit', 'states', ax5)
    draw_scatter(ms, 'distance', 'iterations', ax6)

    # Boxplots
    fig, (ax1, ax2) = plt.subplots(1, 2)
    draw_boxplot(ms,'params', 'time', ax1)
    draw_boxplot(ms,'states', 'time', ax2)
    plt.subplots_adjust(top=0.95, right=0.95, bottom=0.09, left=0.05)
    plt.show()



if __name__ == '__main__':
    main()
