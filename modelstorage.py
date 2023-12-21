import csv
from typing import List
import matplotlib.pyplot as plt
import numpy as np
from model import Model


class ModelStorage:
    def __init__(self):
        self.data: List[Model] = []
        self.fieldnames = ['index', 'states', 'params', 'trial', 'time', 'distance', 'iterations', 'res_fit',
                           'goal_fit', 'miss_fit_flag', 'alg']
        # типы полей
        # index убран
        # True - категориальные, False - количественные
        self.fieldtypes = [False, False, False, False, False, False, False, False, True, True]

    def load_from_file(self, filename='file1.csv'):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, self.fieldnames, delimiter=';')
            i = 0
            for row in reader:
                if i == 0:
                    i += 1
                    continue
                self.data.append(Model(row))

    def get_size_of_data(self):
        return len(self.data)

    def get_count_of_var(self):
        return len(self.fieldnames) - 1

    def get_types_of_vars(self):
        return {self.fieldnames[i+1]: self.fieldtypes[i] for i in range(len(self.fieldtypes))}

    def _get_min_and_max_for_field(self, fieldname):
        values = self._get_values_by_fieldname(fieldname)

        return min(values), max(values)

    def get_ranges_for_all_fields(self):
        return {fieldname: self._get_min_and_max_for_field(fieldname) for fieldname in self.fieldnames[1:]}

    def _get_zero_count_for_field(self, fieldname):
        values = self._get_values_by_fieldname(fieldname)

        return values.count(0)

    def get_zero_count_for_all_fields(self):
        fields = ['time', 'distance', 'iterations']
        return {fieldname: self._get_zero_count_for_field(fieldname) for fieldname in fields}

    def _get_algorithms_set(self):
        return set(self._get_values_by_fieldname('alg'))

    def get_all_models_for_alg(self):
        counts = {alg: 0 for alg in self._get_algorithms_set()}

        for model in self.data:
            counts[model.alg] += 1

        return counts

    def _get_values_by_fieldname(self, fieldname):
        return [getattr(model, fieldname) for model in self.data]

    def _get_values_by_specified_param(self, fieldname1, fieldname2, fieldname1_value):
        data = []
        for model in self.data:
            if getattr(model, fieldname1) == fieldname1_value:
                data.append(getattr(model, fieldname2))

        return data

    def get_histogram_data(self, fieldname):
        return self._get_values_by_fieldname(fieldname)

    def get_scatter_data(self, fieldname1, fieldname2):
        data_1 = self._get_values_by_fieldname(fieldname1)
        data_2 = self._get_values_by_fieldname(fieldname2)
        return data_1, data_2

    def get_boxplot_data(self, fieldname1, fieldname2):

        data_1 = self._get_values_by_fieldname(fieldname1)
        data_2 = self._get_values_by_fieldname(fieldname2)
        data_1 = list(set(data_1))
        data_1.sort()

        data = []
        for el in data_1:
            data.append(self._get_values_by_specified_param(fieldname1, fieldname2, el))

        return data, data_1, min(data_2), max(data_2)


