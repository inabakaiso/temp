import xgboost as xgb
import numpy as np
from sklearn.model_selection import Kfold


def cross_validation(train_x, train_y):
    kf = KFold(n_splits, shuffle=true, random_state=42)
    for tr_idx, va_idx in kf.split(df):
        tr_x, va_x = train_x.iloc[tr_idx], train_x.iloc[va_idx]
        tr_y, va_y = train_y.iloc[tr_idx], train_y.iloc[va_idx]
        
    return tr_x,tr_y,va_x,va_y

def run_xgboost(tr_x, tr_y, va_x, va_y):
    # データのセット
    validation = va_x is not None
    dtrain = xgb.DMatrix(tr_x, label=tr_y)
    if validation:
        dvalid = xgb.DMatrix(va_x, label=va_y)
    
    params_xgb = {
        'objective': 'multi:softprob',
        'eval_metric': 'mlogloss',
        'num_class': 9,
        'max_depth': 12,
        'eta': 0.1,
        'min_child_weight': 10,
        'subsample': 0.9,
        'colsample_bytree': 0.8,
        'silent': 1,
        'random_state': 71,
        'num_round': 10000,
        'early_stopping_rounds': 10,
    }
    
    model = xgb.XGBClassifier(tr_x, tr_y,
                            params_xgb, eval_set(va_x, va_y)) # or XGBLegressor
    return model

    
    
