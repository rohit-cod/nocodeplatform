from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error,mean_absolute_percentage_error,mean_squared_log_error
from data_test.data_pipeline import fetch_data_from_mongo
from models.regression.model_evaluation import fit_and_evaluate_model
import pickle

def run_models():
    # X_train, X_test, y_train, y_test = fetch_data_from_file()
    X_train, X_test, y_train, y_test = fetch_data_from_mongo()
    models = {"LinearRegression": LinearRegression(),
              "GradiantBoost": GradientBoostingRegressor(),
              #"RandomForest": RandomForestRegressor(),
              "XgBoost": XGBRegressor(verbose=0),
              "DecisionTreeRegressor": DecisionTreeRegressor(),
              "CatBoost": CatBoostRegressor(verbose=0),
              "LightGBM": LGBMRegressor()}
    scores = {}
    for name, model in models.items():
        scores[name], retmodel = fit_and_evaluate_model(model, X_train, y_train, X_test, y_test, r2_score)
        pickle.dump(retmodel, open('models/pickle/' + name + '.pkl', 'wb'))
    for item in scores:
        print(item, scores[item])

def evaluate_models():
    X_train, X_test, y_train, y_test = fetch_data_from_mongo()
    models = ["LinearRegression",
              "GradiantBoost",
              #"RandomForest",
              "XgBoost",
              "DecisionTreeRegressor",
              "CatBoost",
              "LightGBM"]
    scores = {}
    for name in models:
        model=pickle.load(open('models/pickle/'+name+".pkl",'rb'))
        y_pred = model.predict(X_test)
        scores[name] = r2_score(y_test, y_pred)
    for item in scores:
        print(item, scores[item])

if __name__ == '__main__':
    #run_models()
    evaluate_models()
