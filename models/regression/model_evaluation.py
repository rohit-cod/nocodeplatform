

def fit_and_evaluate_model(model,X_train,y_train,X_test,y_test,score_metric):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = score_metric(y_test, y_pred)
    return score