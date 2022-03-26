import pandas as pd

df = pd.read_csv('enjoy_sport.csv')
concepts = df.values[:, :-1]
target = df.values[:, -1]

def candidate():
    specific_h = concepts[0][:]
    general_h = [['?' for i in range(len(specific_h))] for i in range(len(specific_h))]
    
    for i, h in enumerate(concepts):
        for x in range(len(specific_h)):
            
            if target[i] == 'yes':
                if h[x] != specific_h[x]:
                    general_h[x][x] = '?'
                    specific_h[x] = '?'
            else:
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
    general_h = [i for i in general_h if ['?'] * len(specific_h)]
    return specific_h, general_h
candidate()
