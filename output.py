import numpy as np

from modelstorage import ModelStorage


# task 1
def output_data_size(ms: ModelStorage):
    print(f'размер выборки: {ms.get_size_of_data()}')


def output_count_vars(ms: ModelStorage):
    print(f'количество переменных: {ms.get_count_of_var()}')


def output_types_of_vars(ms: ModelStorage):
    m = ms.get_types_of_vars()

    for key, value in m.items():
        k = 'категориальной' if value else 'количественной'
        print(f'{key} является {k} переменной')


def output_ranges_of_vars(ms: ModelStorage):
    m = ms.get_ranges_for_all_fields()
    for key, value in m.items():
        print(f'для {key} минимальное значение: {value[0]}, а максимальное значение: {value[1]} ')


def output_zero_count_of_vars(ms: ModelStorage):
    m = ms.get_zero_count_for_all_fields()
    for key, value in m.items():
        print(f'для {key} отсутствует {value} значений ')


# task 6

def output_counts_of_model_by_algo(ms: ModelStorage):
    m = ms.get_all_models_for_alg()
    for key, value in m.items():
        print(f'по алгоритму {key} найдено {value} наблюдений')


# task 2

def draw_histogram(ms: ModelStorage, fieldname, ax):
    data = ms.get_histogram_data(fieldname)
    pockets_c = 20
    y, x, _ = ax.hist(data, bins=pockets_c, linewidth=0.5, edgecolor="white")
    max_y = round(int(y.max()) + 10, -1)
    max_x = round(int(x.max()) + 10, -1)
    ax.set_title(f'Гистограмма распределения {fieldname}', fontsize=18)

    ax.set(ylim=(0, max_y), yticks=np.linspace(0, max_y, 11),
           xlim=(x.min() - 10, x.max() + 10), xticks=(np.arange(0, max_x, max_x // pockets_c)))
    ax.tick_params(labelrotation=-70)


def draw_scatter(ms: ModelStorage, fieldname1, fieldname2, ax):
    data_1, data_2 = ms.get_scatter_data(fieldname1, fieldname2)
    ax.scatter(data_1, data_2)
    ax.set_title(f'{fieldname1} и {fieldname2} - диаграмма рассеяния', fontsize=18)
    ax.set_xlabel(fieldname1, fontsize=16)
    ax.set_ylabel(fieldname2, fontsize=16)
    ax.set(xlim=(0, max(data_1) * 1.1),
           ylim=(0, max(data_2) * 1.1))
    ax.tick_params(labelrotation=-50)


def draw_boxplot(ms: ModelStorage, fieldname1, fieldname2, ax):
    data, data_1, min_y, max_y = ms.get_boxplot_data(fieldname1, fieldname2)
    VP = ax.boxplot(data, positions=data_1, widths=0.5)
    ax.set_title(f'{fieldname1} и {fieldname2}', fontsize=18)
    ax.set_xlabel(fieldname1, fontsize=16)
    ax.set_ylabel(fieldname2, fontsize=16)
    ax.set(xlim=(min(data_1) - 1, max(data_1) + 1),
           ylim=(min_y, max_y + 10))


