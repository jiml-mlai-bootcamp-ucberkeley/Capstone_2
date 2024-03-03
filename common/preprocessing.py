
import pandas as pd
from sklearn.preprocessing import normalize, MinMaxScaler

def mean_and_std(what):
    data = what["data"]
    features_a = what["features_a"]
    features_n = what["features_n"]
    
    normalized_df = pd.DataFrame()
    
    if len(features_n) > 0:
        for feature in features_n:
            not_normalized = data[feature]
            normalized_df[feature] = (not_normalized - not_normalized.mean())/not_normalized.std()
            #normalized_df = pd.DataFrame(normalized_data, columns=features_n)

    if len(features_a) > 0:
        for feature in features_a:
            normalized_df[feature] = data[feature].values

    return normalized_df

def normalizer(what):
    data = what["data"]
    features_a = what["features_a"]
    features_n = what["features_n"]
    
    normalized_df = pd.DataFrame()
    
    if len(features_n) > 0:
        not_normalized_df = data[features_n]
        normalized_data = normalize(not_normalized_df, axis=0)
        normalized_df = pd.DataFrame(normalized_data, columns=features_n)
        
    for feature in features_a:
        normalized_df[feature] = data[feature].values
        
    return normalized_df

def scaleminmax(what):
    data = what["data"]
    features_a = what["features_a"]
    features_n = what["features_n"]
    
    normalized_df = pd.DataFrame()
    
    if len(features_n) > 0:
        scaler = MinMaxScaler()
        not_normalized_df = data[features_n]
        normalized_data = scaler.fit_transform(not_normalized_df)
        normalized_df = pd.DataFrame(normalized_data, columns=features_n)
        
    for feature in features_a:
        normalized_df[feature] = data[feature].values
        
    return normalized_df