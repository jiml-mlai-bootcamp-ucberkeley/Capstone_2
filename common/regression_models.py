
from print_more_stuff import print_more_stuff

from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import SequentialFeatureSelector, RFE
from sklearn.model_selection import train_test_split, GridSearchCV

def dosomething(kind,title,df,features,what):

    num_features_to_select = len(features)-1
    random_state_value = 42
    
    match kind:
        case "Decision Tree":
            estimator = DecisionTreeRegressor()
    
    X = df[features]
    y = df[what]
    
    match title:
        case "Recursive Feature Elimination":
            dtree = RFE(estimator, n_features_to_select=num_features_to_select)
        case "Sequential Feature Selector":
            dtree = SequentialFeatureSelector(estimator, n_features_to_select=num_features_to_select)
        
    dtree.fit(X, y)
    dtree_selected_features = dtree.get_support()
    print('The selected features are:', list(X.columns[dtree_selected_features]))
    
    X = df[list(X.columns[dtree_selected_features])]
    y = df[what]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state_value)
    
    
    dtree_gscv = GridSearchCV(estimator,param_grid={})
    dtree_model = dtree_gscv.fit(X_train,y_train)
    dtree_predict = dtree_model.predict(X_test)
    
    rtnval = print_more_stuff(title, y_test, dtree_predict, dtree_gscv)
    
    return rtnval