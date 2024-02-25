
import pandas as pd
from sklearn.preprocessing import normalize

def normalizer(what):
    data = what["data"]
    features_a = what["features_a"]
    features_n = what["features_n"]
    
    not_normalized_df = data[features_n]
    normalized_data = normalize(not_normalized_df)
    normalized_df = pd.DataFrame(normalized_data, columns=features_n)
    for feature in features_a:
        normalized_df[feature] = data[feature]
    return normalized_df