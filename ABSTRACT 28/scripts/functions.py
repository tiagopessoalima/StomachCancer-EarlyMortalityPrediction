# standard Python imports
import ast
import pandas as pd

def best_features_set(model_name):
    evaluations_folder = '../evaluations/'
    evaluations = pd.read_csv(f'{evaluations_folder}/{model_name}.csv')
    evaluations['feature_count'] = evaluations['Features'].apply(lambda x: len(ast.literal_eval(x)))
    evaluations_sorted = evaluations.sort_values(by=['Fitness', 'feature_count'], ascending=[False, True])
    index_max_fitness_min_features = evaluations_sorted.index[0]
    best_features = evaluations_sorted.loc[index_max_fitness_min_features, 'Features']
    return ast.literal_eval(best_features)
