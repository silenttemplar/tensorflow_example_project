import numpy as np
import csv

def bop_data_reader(file_path='./BrentOilPrices.csv'):
    #absolute_path = os.path.dirname(os.path.abspath(__file__))
    #file_path = absolute_path + '\dataset\BrentOilPrices.csv'

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_dict = {month_list[m_idx]: m_idx + 1 for m_idx in range(len(month_list))}

        dataset = list()
        for data in csv_reader:
            #print(data)
            price = data[-1]
            data = data[0]

            try:
                D, M, Y = data.split(sep='-')
                if int(Y) >= 87:
                    M = month_dict[M]
                    dataset.append([Y, M, D, price])
            except:
                pass

    dataset = np.array(dataset).astype(np.float)
    return dataset

def get_year_data(dataset, t_year):
    t_idx  = np.where(dataset[:,0] == t_year)
    t_data = dataset[t_idx]
    return t_data

if __name__ == '__main__':
    dataset = bop_data_reader()
    #print(dataset)

    year90_data = get_year_data(dataset, 90)
    #print(year90_data)