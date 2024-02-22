
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score


def print_more_stuff(title, y_param, predict_param, gscv):
    
    results_dict = {"model":"", "explained variance score":0,"mae score":0,"mse score":0,"r2 score":0, "mean fit time":0}
    results_dict["model"] = title
    
    evs = "{:.9f}".format(explained_variance_score(y_param,predict_param))
    mae = "{:,.6f}".format(mean_absolute_error(y_param,predict_param))
    mse = "{:,.6f}".format(mean_squared_error(y_param,predict_param))
    r2 = "{:,.6f}".format(r2_score(y_param,predict_param))
    
    #find_best_params = gscv.cv_results_["params"].index(gscv.best_params_)
    #mean_fit_time = gscv.cv_results_["mean_fit_time"][find_best_params]
    mean_fit_time = gscv.cv_results_["mean_fit_time"][gscv.best_index_]
    
    results_dict["explained variance score"] = evs
    results_dict["mae score"] = mae
    results_dict["mse score"] = mse
    results_dict["r2 score"] = r2
    results_dict["mean fit time"] = mean_fit_time
    
    print(title + " EVS = " + evs)
    print(title + " MSE = " + mse)
    print(title + " MAE = " + mae)
    print(title + " R2 = " + r2)
    print(title + " Fit Time = " + str(mean_fit_time))
    
    return results_dict