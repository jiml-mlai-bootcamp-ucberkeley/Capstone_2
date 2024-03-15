
from print_more_stuff import print_more_stuff

import numpy as np
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.feature_selection import SequentialFeatureSelector, RFE, SelectFromModel
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# Create models and feature selections in one file instead of each Notebook

def dosomething(kind,title,df,features,target,best_params={}):

    num_features_to_select = len(features)-1
    random_state_value = 42
    grid_params = {}
    
    estimator = LinearRegression()
    
    match kind:
        case "Decision Tree":
            estimator = DecisionTreeRegressor(**best_params)
        case "Ada Boost":
            estimator = AdaBoostRegressor(**best_params)
        case "Gradient Boosting":
            estimator = GradientBoostingRegressor(**best_params)
        case "Hist Gradient Boosting":
            estimator = HistGradientBoostingRegressor(**best_params)
        case "Random Forest":
            estimator = RandomForestRegressor(**best_params)
        case "KNearset Neighbors":
            estimator = KNeighborsRegressor(**best_params)
        case "Lasso":
            estimator = Lasso(**best_params)
        case "Linear":
            estimator = LinearRegression()
        case "Ridge":
            estimator = Ridge(**best_params)
    
    X = df[features]
    y = df[target]
    
    feature_selections = ["Recursive Feature Elimination", "Sequential Feature Selector", "Select From Model"]
    #if title != "" and title != "PolynomialFeatures" and title.find("Best Params") == -1:

    if title in feature_selections:
        match title:
            case "Recursive Feature Elimination":
                something = RFE(estimator, n_features_to_select=num_features_to_select)
            case "Sequential Feature Selector":
                something = SequentialFeatureSelector(estimator, n_features_to_select=num_features_to_select)
            case "Select From Model":
                something = SelectFromModel(estimator)
                
        something.fit(X, y)
        something_selected_features = something.get_support()
        if True not in something_selected_features:
            howmany = len(something_selected_features)
            alltrue = np.empty(howmany, dtype=bool)
            alltrue.fill(True)
            something_selected_features = alltrue

        print('The selected features are:', list(X.columns[something_selected_features]))
        X = df[list(X.columns[something_selected_features])]
        y = df[target]
    elif title == "PolynomialFeatures":
        estimator = Pipeline([
            ('poly_features', PolynomialFeatures()), 
            ('poly_model', LinearRegression(fit_intercept=True))
        ])
        grid_params = best_params
    else:
        print('The selected features are:', features)
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state_value)
    
    
    something_gscv = GridSearchCV(estimator,param_grid=grid_params)
    something_model = something_gscv.fit(X_train,y_train)
    something_predict = something_model.predict(X_test)
    
    results = print_more_stuff(title, y_test, something_predict, something_gscv)
    rtnval = {"results":results, "predictions":something_predict}
    
    return rtnval