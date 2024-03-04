
from print_more_stuff import print_more_stuff

from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import SequentialFeatureSelector, RFE
from sklearn.model_selection import train_test_split, GridSearchCV

def dosomething(kind,title,df,features,what,best_params={}):

    num_features_to_select = len(features)-1
    random_state_value = 42
    
    match kind:
        case "Decision Tree":
            estimator = DecisionTreeRegressor(**best_params)
        case "Ada Boost":
            estimator = AdaBoostRegressor(**best_params)
    
    X = df[features]
    y = df[what]
    
    if title.find("Best Params") == -1:
        match title:
            case "Recursive Feature Elimination":
                something = RFE(estimator, n_features_to_select=num_features_to_select)
            case "Sequential Feature Selector":
                something = SequentialFeatureSelector(estimator, n_features_to_select=num_features_to_select)

        something.fit(X, y)
        something_selected_features = something.get_support()
        print('The selected features are:', list(X.columns[something_selected_features]))

        X = df[list(X.columns[something_selected_features])]
        y = df[what]
    else:
        print('The selected features are:', features)
        something = estimator
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state_value)
    
    
    something_gscv = GridSearchCV(estimator,param_grid={})
    something_model = something_gscv.fit(X_train,y_train)
    something_predict = something_model.predict(X_test)
    
    results = print_more_stuff(title, y_test, something_predict, something_gscv)
    rtnval = {"results":results, "predictions":something_predict}
    
    return rtnval