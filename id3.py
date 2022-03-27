from collections import Counter
import pandas as pd
import numpy as np
import math

def entropy(xs:list):
    import math
    return sum([ -x * math.log2(x) for x in xs ])

def entropy_of_list(xs:list):
    cnt = Counter(x for x in xs)
    n = len(xs)
    prob = [ x/n for x in cnt.values() ]
    return entropy(prob)

def info_gain(df:pd.DataFrame, split, target):
    df_split = df.groupby(split)
    n = len(df)
    df_arg_ent = df_split.agg({target: [entropy_of_list, lambda x : len(x) / n ]})[target]
    df_arg_ent.columns = ['entropy', 'prob_obs']
    new_entropy = sum( df_arg_ent['entropy'] * df_arg_ent['prob_obs'] )
    old_entropy = entropy_of_list(df['target'])
    return old_entropy - new_entropy

def id3(df:pd.DataFrame, target:str, attribute:list[str], default_class:str=None):
    cnt = Counter(x for x in df['target'])
    
    if len(cnt) == 1 :
        return next(iter(cnt))
    
    elif df.empty or not attribute:
        return default_class
    
    else:
        default_class = max(cnt.keys())
        gains = [ info_gain(df, attr, target) for attr in attribute ]
        index_of_max = gain.index(max(gain))
        best_attr = attribute[index_of_max]
        tree = {best_attr: {}}
        remaining = [ i for i in attribute if i != best_attr ]
        
        for attr_val, subset in df.groupby(best_attr):
            subtree = id3(subset, target, remaining, default_class)
            tree[best_attr][attr_val] = subtree
        return tree

df = pd.read_csv('playtennis.csv')
total_entrop = entropy_of_list(df['play_tennis'])
attribute = list(df.columns[:-1])
tree = id3(df, target, attribute)
pprint(tree)

def test(tree, test_data):
    for tree_key in tree:
        for tree_val in tree[tree_key]:
            if test_data[tree_key] == tree_val and isinstance(tree[tree_key][tree_val], dict):
                test(tree[tree_key][tree_val], test_data)
            elif test[tree_key] == tree_value:
                print('Classififcation:\t', tree[tree_key][tree_val])

test(tree, df.iloc[2:, 3])
    
