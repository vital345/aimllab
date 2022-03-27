import numpy as np
import csv

# read csv file 
with open('playtennis.csv') as f:
    data = csv.reader(f)
    train = []
    
    for row in data:
        train.append(row)
    train = train[1:]
X = np.array(train)

# naive bayes function
def classify(train:np.array, test:np.array):
    total_size = len(train)
    print('training data size:\t', total_size)
    print('testing data size:\t', test.shape[0])
    
    target = np.unique(train[:, -1])
    count = np.zeros((target.shape[0]), dtype=int)
    prob = np.zeros((target.shape[0]), dtype=float)
    
    for row in train:
        if row[-1] == target[0]:
            count[0] += 1
        else:
            count[1] += 1
    prob[0] = count[0] / total_size
    prob[1] = count[1] / total_size
    
    print(f"total {target[1]}:\t", prob[1])
    print(f"total {target[0]}:\t", prob[0])
    
    prob0 = np.zeros((test.shape[1]-1), dtype=float)
    prob1 = np.zeros((test.shape[1]-1), dtype=float)
    
    print('instance pred  actual\t')
    accuracy = 0
    
    for t in range(test.shape[0]):
        for k in range(test.shape[1]-1):
            count0 = 0
            count1 = 0
            for j in range(train.shape[0]):
                if test[t, k] == train[j, k] and train[j, -1] == target[0]:
                    count0 += 1
                elif test[t, k] == train[j, k] and train[j, -1] == target[1]:
                    count1 += 1
            prob0[k] = count0 / count[0]
            prob1[k] = count1 / count[1]
        
        prob_yes = prob[1]
        prob_no = prob[0]
        
        for col in range(test.shape[1]-1):
            prob_yes *= prob1[col]
            prob_no *= prob0[col]
        
        if prob_no > prob_yes:
            predict = target[0]
        else:
            predict = target[1]
        
        print(t+1, "\t", predict, "\t", test[t, -1])
        
        if predict == test[t, -1]:
            accuracy += 1
    print("total correct prediction:\t", accuracy)
    print("final accuracy of model :\t", (accuracy / total_size) * 100)
    return

classify(X, X)
    
    
