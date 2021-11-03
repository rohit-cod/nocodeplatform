from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error,mean_absolute_percentage_error,mean_squared_log_error
from data_test.data_pipeline import fetch_data_from_mongo
from models.regression.model_evaluation import fit_and_evaluate_model

if __name__ == '__main__':
    #X_train, X_test, y_train, y_test = fetch_data_from_file()
    X_train, X_test, y_train, y_test = fetch_data_from_mongo()
    models = {"LinearRegression": LinearRegression(),
          "GradiantBoost": GradientBoostingRegressor(),
          "RandomForest": RandomForestRegressor(),
          "XgBoost": XGBRegressor(verbose=0),
          "DecisionTreeRegressor": DecisionTreeRegressor(),
          "CatBoost": CatBoostRegressor(verbose=0),
          "LightGBM": LGBMRegressor()}
    scores={}
    for name, model in models.items():
        scores[name]=fit_and_evaluate_model(model,X_train, y_train, X_test, y_test,r2_score)
    for item in scores:
        print(item, scores[item])
