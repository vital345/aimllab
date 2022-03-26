import numpy as np

def ann():
    X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
    y = np.array(([92], [86], [89]), dtype=float)
    # scale the values of X
    X = X / np.amax(X, axis=0) # axis=0 means column wise maximum
    y = y / 100
    
    #set values
    lr = 0.24
    input_layer = 2
    hidden_layer = 3
    output_layer = 1
    epoch = 5000
    
    wh = np.random.uniform(size=(input_layer, hidden_layer))
    bh = np.random.uniform(size=(1, hidden_layer))    
    wo = np.random.uniform(size=(hidden_layer, output_layer))    
    bo = np.random.uniform(size=(1, output_layer))
    
    for _ in range(epochs):
        # forward prop
        net_h = np.dot(X, wh) + bh
        sigma_h = activate(net_h)
        
        net_o = np.dot(sigma_h, wo) + bo
        output = activate(net_o)
        
        error = y - output
        # backward prop
        delta_k = error * activate(net_o, True)
        delta_h = delta_k * activation(sigma_h, True)
        
        wo += sigma_h.T.dot(delta_k) * lr
        wh += X.T.dot(delta_h) * lr
    
    print('Input:\t', X)
    print('Actual Output:\t', y)
    print('Predicted Output:\t', output)
    return

def activate(x, derivative=False):
    if derivative:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

ann()
