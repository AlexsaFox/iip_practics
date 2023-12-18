class Model:
    def __init__(self, data):
        self.index = int(data['index'])
        self.states = int(data['states'])
        self.params = int(data['params'])
        self.trial = int(data['trial'])
        self.time = float(data['time'].replace(',', '.'))
        self.distance = float(data['distance'].replace(',', '.'))
        self.iterations = int(data['iterations'])
        self.res_fit = float(data['res_fit'].replace(',', '.'))
        self.goal_fit = float(data['goal_fit'].replace(',', '.'))
        self.miss_fit_flag = int(data['miss_fit_flag'])
        self.alg = int(data['alg'])

    def __str__(self):
        return f'index:{self.index} alg:{self.alg}'
