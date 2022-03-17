import pandas as pd
import helper as h

class Generic:

    # excel data reading, with dict as returned item
    def read_excel(self):
        file_loc = './data/case_1.xls'
        project = {}
        file = pd.read_excel(file_loc)
        for i, j in file.iterrows():
            if (i != 0):
                project_name = file.iat[i, 1]
                processing_time = int(file.iat[i, 2])
                weight = int(file.iat[i, 3])
                due_date = int(file.iat[i, 4])
                project[project_name] = {
                    'p': processing_time,
                    'w': weight,
                    'd': due_date
                }
        return project

    # convert dictionary to list, for randoming solutions
    def convert_dict_to_list(self, raw_data):
        project = raw_data
        
        data = []
        for a in project:
            chromosome = []
            chromosome.append(a)
            chromosome.append(project[a]['p'])
            chromosome.append(project[a]['w'])
            chromosome.append(project[a]['d'])
            for _ in range(4):
                chromosome.append(0)
            data.append(list(chromosome))
        return data