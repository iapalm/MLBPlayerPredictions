import numpy as np


def load_data():
    try:
        data = np.load('../data/gen/batting.npy').item()
        return data
    except:
        return read_data()
        

def read_data():
    print("reading data")
    data = dict()
    db_file = open('../data/baseballdatabank-master/core/Batting.csv')
    
    col_labels = []
    for line in db_file:
        words = line.split(',')

        if words[0] == 'playerID': # don't read first line
            col_labels = [w.strip() for w in words]
            continue

        key = (words[0], int(words[1]))
        if key in data: # other stints
            for i in range(5, len(words)):
                if words[i].strip() != '':
                    feature[col_labels[i]] += int(words[i].strip())
        else:
            feature = {col_labels[3]:words[3], col_labels[4]:words[4]} # team, league
            for i in range(5, len(words)):
                if words[i].strip() != '':
                    feature[col_labels[i]] = int(words[i].strip())
                else:
                    feature[col_labels[i]] = 0

            data[(words[0], int(words[1]))] = feature
    np.save('../data/gen/batting.npy', data)
    return data

